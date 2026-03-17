"""
App Flask: predicción de riesgo de remociones en masa (CDMX).
Formulario web con 16 variables → servidor devuelve probabilidad y nivel de riesgo.
"""
import os
import joblib
from flask import Flask, request, render_template
import numpy as np

# Mismo orden que en Proyecto.ipynb
FEATURE_COLS = [
    "dist_falla_m",
    "dist_fractura_m",
    "en_hundimiento",
    "en_agrietamiento",
    "tiene_litologia",
    "tiene_suelo",
    "en_topoforma",
    "lon",
    "lat",
    "tiene_inestabilidad",
    "precip_1d",
    "precip_7d",
    "precip_15d",
    "precip_30d",
    "max_intensity_7d",
    "consecutive_rainy_days",
]

app = Flask(__name__)

# Cargar modelo y scaler al arrancar
ARTIFACTS_DIR = os.path.join(os.path.dirname(__file__), "app_artifacts")
model = None
scaler = None


def load_artifacts():
    global model, scaler
    if model is not None and scaler is not None:
        return
    model_path = os.path.join(ARTIFACTS_DIR, "model.keras")
    scaler_path = os.path.join(ARTIFACTS_DIR, "scaler.pkl")
    if not os.path.isfile(model_path) or not os.path.isfile(scaler_path):
        raise FileNotFoundError(
            "Faltan app_artifacts/model.keras o app_artifacts/scaler.pkl. "
            "Desde el notebook ejecuta: %run export_artifacts.py"
        )
    from tensorflow import keras

    model = keras.models.load_model(model_path)
    scaler = joblib.load(scaler_path)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    load_artifacts()
    data = request.form
    try:
        vector = []
        for col in FEATURE_COLS:
            val = data.get(col, "").strip()
            if val == "":
                return render_template(
                    "index.html",
                    error=f"Falta el campo: {col}",
                ), 400
            if col in (
                "en_hundimiento",
                "en_agrietamiento",
                "tiene_litologia",
                "tiene_suelo",
                "en_topoforma",
                "tiene_inestabilidad",
            ):
                vector.append(1 if val.lower() in ("1", "true", "sí", "si", "yes") else 0)
            else:
                vector.append(float(val))
        X = np.array([vector], dtype=np.float64)
        X_scaled = scaler.transform(X)
        prob = float(model.predict(X_scaled, verbose=0)[0][0])
        level = "Alto" if prob > 0.7 else ("Medio" if prob > 0.4 else "Bajo")
        return render_template(
            "index.html",
            prediction=True,
            probability=prob,
            level=level,
        )
    except ValueError as e:
        return render_template("index.html", error=str(e)), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
