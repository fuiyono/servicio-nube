# Artefactos del modelo

Coloca aquí los archivos generados después de entrenar el modelo en el proyecto principal:

- **model.keras** – modelo Keras guardado
- **scaler.pkl** – StandardScaler (joblib)
- **feature_cols.pkl** – lista de nombres de columnas (opcional para la app)

Desde el proyecto principal (donde está `Proyecto.ipynb`), después de entrenar:

```python
%run export_artifacts.py
```

Luego copia el contenido de `app_artifacts/` de ese proyecto a esta carpeta (o configura `export_artifacts.py` para que guarde directamente en `servicio-nube/app_artifacts/`).
