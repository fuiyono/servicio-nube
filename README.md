# Servicio en la nube – Predicción de riesgo de remociones en masa (CDMX)

Aplicación Flask para predecir riesgo de remociones en masa a partir de 16 variables (estáticas y de precipitación). Pensada para desplegar en **AWS EC2** (Ubuntu).

## Contenido del repositorio

- **app.py** – Aplicación Flask (GET `/`, POST `/predict`)
- **templates/index.html** – Formulario web con las 16 variables
- **app_artifacts/** – Carpeta para el modelo y el scaler (ver más abajo)
- **requirements.txt** – Dependencias para el servidor

## Antes del primer deploy: artefactos del modelo

La app necesita en `app_artifacts/`:

- `model.keras`
- `scaler.pkl`

Generados en el proyecto principal (notebook) con:

```python
%run export_artifacts.py
```

Copia esos archivos desde el proyecto principal a esta carpeta `app_artifacts/` antes de subir a GitHub o al servidor.

## Despliegue en EC2 (Ubuntu)

1. **Clonar en la instancia**
   ```bash
   git clone git@github.com:fuiyono/servicio-nube.git
   cd servicio-nube
   ```

2. **Entorno virtual e instalación**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Probar la app**
   ```bash
   python app.py
   ```
   O en producción con Gunicorn:
   ```bash
   gunicorn -w 1 -b 0.0.0.0:5000 app:app
   ```

4. **Abrir puerto en AWS**  
   Security Group → Inbound → TCP 5000 (o 80 si usas proxy).

5. **Acceder**  
   `http://<IP-pública-EC2>:5000`

## Uso

En la web se muestra un formulario con las 16 variables. Tras enviar, el servidor devuelve la probabilidad de riesgo y el nivel (Bajo / Medio / Alto).
