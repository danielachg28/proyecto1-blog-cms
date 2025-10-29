# Dockerfile (producción)
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.txt

COPY . /app/

# Crear directorio temporal y asignar permisos
RUN mkdir -p /tmp && chmod 1777 /tmp


EXPOSE 8000

CMD ["gunicorn", "blog.wsgi:application", "--bind", "0.0.0.0:8000"]
