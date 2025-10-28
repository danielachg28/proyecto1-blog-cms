# Dockerfile
FROM python:3.12-slim

# Evita archivos pyc y habilita logs en buffer
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo
WORKDIR /app

# Instalar herramientas necesarias para Cursor Server y dependencias del proyecto
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    bash \
    sudo \
 && rm -rf /var/lib/apt/lists/*


# Copiar requirements.txt e instalar dependencias
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar el resto del proyecto
COPY . /app/

 # Instalar Cursor Server
 RUN curl -fsSL https://install.cursor.so/latest | bash

# Exponer puertos: 8000 Django y 5678 para debug
EXPOSE 8000 5678

# Comando por defecto: levantar Django y esperar debugger
CMD ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "--wait-for-client", "manage.py", "runserver", "0.0.0.0:8000"]
