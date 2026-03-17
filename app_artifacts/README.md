# Artefactos del modelo

En este repo ya están **scaler.pkl** y **feature_cols.pkl**.

Falta **model.keras**. Opciones:

1. **Modelo real (recomendado)**  
   En el proyecto principal (donde está `Proyecto.ipynb`), ejecuta todas las celdas hasta el entrenamiento y la celda de exportación. Luego copia aquí `app_artifacts/model.keras` desde ese proyecto.

2. **Modelo de ejemplo (misma arquitectura, para probar la app)**  
   Donde tengas TensorFlow instalado, en la raíz de este repo:
   ```bash
   python generate_model_keras.py
   ```
   Eso crea `app_artifacts/model.keras` y la app ya puede servir predicciones.
