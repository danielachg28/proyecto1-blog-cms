#!/bin/bash

set -e  # detiene el script si algún comando falla

# Opcional: mostrar en logs el PORT que Railway asignó
echo "Railway PORT: $PORT"

# Instalar dependencias
pip install --no-cache-dir --upgrade pip
pip install --no-cache-dir -r requirements.txt

# Aplicar migraciones automáticamente
python manage.py migrate --noinput

# Arrancar Gunicorn usando el puerto asignado por Railway
# Si $PORT no está definido, usar 8000 como fallback
gunicorn blog.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3
