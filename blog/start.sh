#!/bin/bash

# Instalar dependencias
pip install -r requirements.txt

# Aplicar migraciones automáticamente
python manage.py migrate --noinput

# Arrancar servidor de producción con Gunicorn
gunicorn blog.wsgi:application --bind 0.0.0.0:$PORT
