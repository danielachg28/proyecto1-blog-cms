# Dockerfile (producción)
FROM python:3.12-slim

# Configuración base de Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Usamos /home/tmp como carpeta temporal (es writable en Sherpa)
ENV TMPDIR=/home/tmp

WORKDIR /app

# Instala dependencias
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia el proyecto
COPY . .

# Crea carpeta temporal y le da permisos
RUN mkdir -p /home/tmp && chmod 777 /home/tmp

# Evita que falle si no hay estáticos
RUN python manage.py collectstatic --noinput --ignore=.gitignore || true

EXPOSE 8000

# Ejecuta gunicorn
CMD ["gunicorn", "blog.wsgi:application", "--bind", "0.0.0.0:8000"]
