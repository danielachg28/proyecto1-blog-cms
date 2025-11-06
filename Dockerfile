# Dockerfile (producción)
FROM python:3.12-slim

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=blog.settings.prod
ENV PYTHONPATH=/app
ENV TMPDIR=/dev/shm

# Directorio de trabajo
WORKDIR /app

# Dependencias de python
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache /tmp/*

# Copiar el resto del proyecto
COPY blog /app/blog

# Dar permisos de ejecución al script de arranque
RUN chmod +x start.sh

# Exponer puerto 8000
EXPOSE 8000

# Usa el script de arranque
CMD ["bash", "start.sh"]
