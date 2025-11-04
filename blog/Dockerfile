# Dockerfile (producción)
FROM python:3.12-slim

# Evitar archivos pyc y habilitar logs en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=blog.settings.prod


# Gunicorn usará /dev/shm (espacio temporal en memoria) para sus archivos temporales
ENV TMPDIR=/dev/shm

WORKDIR /app

# Instalar dependencias
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar el proyecto
COPY . .

EXPOSE 8000

# Ejecutar Gunicorn especificando su tmpdir también
CMD python manage.py collectstatic --noinput && \
    gunicorn blog.wsgi:application --bind 0.0.0.0:8080 --worker-tmp-dir /dev/shm
# CMD ["gunicorn", "blog.wsgi:application", "--bind", "0.0.0.0:8080", "--worker-tmp-dir", "/dev/shm"]
