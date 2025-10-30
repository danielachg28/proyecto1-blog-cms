# Dockerfile (producción)
# Dockerfile (producción)
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Le dice a Python dónde escribir archivos temporales
ENV TMPDIR=/app/tmp

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

COPY . /app/

# Crear directorio temporal dentro de /app
RUN mkdir -p /app/tmp

# (opcional) Recoger estáticos, sin romper si no existen
RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

# Iniciar Gunicorn normalmente
CMD ["gunicorn", "blog.wsgi:application", "--bind", "0.0.0.0:8000"]
