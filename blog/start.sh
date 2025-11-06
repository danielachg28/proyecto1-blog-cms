#!/bin/bash

set -e  # detiene el script si algún comando falla

# Opcional: mostrar en logs el PORT que Railway asignó
echo "Railway PORT: $PORT"

# Aplicar migraciones automáticamente
python manage.py migrate --noinput

# 🔧 NUEVO: recopilar archivos estáticos antes de arrancar
echo "Ejecutando collectstatic..."
python manage.py collectstatic --noinput

# Arrancar Gunicorn usando el puerto asignado por Railway
echo "Iniciando Gunicorn..."
gunicorn blog.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3 --worker-tmp-dir /dev/shm
