"""
Genera app_artifacts/model.keras con la misma arquitectura que el proyecto
(16 → 128 → 64 → 32 → 1). Ejecutar donde TensorFlow funcione:

  python generate_model_keras.py

Para el modelo real entrenado con datos, usa el proyecto principal:
  Abre Proyecto.ipynb, ejecuta hasta la celda de entrenamiento, luego la celda de exportación.
  Copia app_artifacts/model.keras aquí.
"""
import os
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

os.makedirs("app_artifacts", exist_ok=True)
input_dim = 16
model = keras.Sequential([
    layers.Dense(128, input_dim=input_dim, activation="relu"),
    layers.Dropout(0.3),
    layers.Dense(64, activation="relu"),
    layers.Dropout(0.2),
    layers.Dense(32, activation="relu"),
    layers.Dropout(0.2),
    layers.Dense(1, activation="sigmoid"),
])
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
X = np.random.randn(100, input_dim).astype(np.float64)
y = (X.sum(axis=1) > 0).astype(np.float32)
model.fit(X, y, epochs=1, verbose=0)
model.save("app_artifacts/model.keras")
print("✓ app_artifacts/model.keras generado")
