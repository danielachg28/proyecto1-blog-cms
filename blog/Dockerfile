# Dockerfile
FROM python:3.12-slim

# Evita archivos pyc y habilita logs en buffer
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo
WORKDIR /app

# Copiar requirements.txt e instalar dependencias
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar el resto del proyecto
COPY . /app/

# Exponer puerto de Django
EXPOSE 8000

# Comando por defecto para levantar Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
