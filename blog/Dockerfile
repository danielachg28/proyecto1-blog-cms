# Dockerfile (producción)
FROM python:3.12-slim

# --- Configuración básica de Python ---
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# --- Define un directorio temporal seguro ---
ENV TMPDIR=/app/tmp

# --- Establece el directorio de trabajo ---
WORKDIR /app

# --- Copia primero requirements para aprovechar cache ---
COPY requirements.txt ./

# --- Instala dependencias ---
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# --- Copia el resto del proyecto ---
COPY . .

# --- Crea y da permisos al directorio temporal ---
# Muy importante: Gunicorn necesita poder escribir en /app/tmp
RUN mkdir -p /app/tmp && chmod 777 /app/tmp

# --- Recoge archivos estáticos solo si aplica ---
# No se debe ejecutar durante el build si usas SQLite o debug, porque no hay settings configurado aún
# Lo marcamos como opcional para no romper la imagen
RUN python manage.py collectstatic --noinput --ignore=.gitignore || true

# --- Expone el puerto de Gunicorn ---
EXPOSE 8000

# --- Comando de inicio ---
CMD ["gunicorn", "blog.wsgi:application", "--bind", "0.0.0.0:8000"]
