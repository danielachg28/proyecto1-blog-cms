# 📰 Blog CMS – Headless CMS con Django

Proyecto que implementa un **CMS (Content Management System)** headless básico utilizando **Django** y **Django REST Framework**.
Permite a los usuarios registrarse, crear un blog personal, gestionar posts y etiquetas, y acceder a los datos mediante una API REST documentada.

---

## 🚀 Tecnologías Utilizadas

| Tecnología                | Uso                           |
| ------------------------- | ----------------------------- |
| **Python 3.14+**          | Lenguaje principal            |
| **Django 5.2,7**            | Framework backend             |
| **Django REST Framework** | API REST                      |
| **django-tinymce**        | Editor HTML en el admin       |
| **django-import-export**  | Exportación de datos          |
| **drf-yasg**              | Documentación Swagger / Redoc |
| **SQLite**                | Base de datos para desarrollo |

---

## ⚙️ Instalación y Configuración

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/danielachg28/proyecto1-blog-cms.git
cd blog-cms
```

### 2️⃣ Crear y activar entorno virtual

```bash
python -m venv myvenv
source myvenv/bin/activate   # En macOS/Linux
myvenv\Scripts\activate      # En Windows
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Crear superusuario

```bash
python manage.py createsuperuser
```

### 6️⃣ Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧩 Funcionalidades Principales

✅ **Registro y login de usuarios**
✅ **Blog personal por usuario** (1:1 con `User`)
✅ **Gestión de posts y etiquetas** desde panel admin y API
✅ **TinyMCE** como editor de texto enriquecido
✅ **Exportación de datos a CSV/JSON** desde el admin
✅ **Autenticación por sesión en API REST**
✅ **Documentación Swagger y Redoc automática**

---

## 🧠 Arquitectura de Modelos

```
User (Django built-in)
└── Blog (1:1 con User)
    └── Post (N:1 con Blog)
        └── Tag (M:N con Post)
```

---

## 🌐 API REST

### Endpoints principales

| Endpoint           | Método     | Descripción                | Autenticación |
| ------------------ | ---------- | -------------------------- | ------------- |
| `/api/register/`   | POST       | Registrar un nuevo usuario | ❌ No requiere |
| `/api-auth/login/` | GET        | Iniciar sesión             | ✅ Sí          |
| `/api/blogs/`      | GET / POST | Ver o crear blogs          | ✅ Sí          |
| `/api/posts/`      | GET / POST | Ver o crear posts          | ✅ Sí          |
| `/api/tags/`       | GET / POST | Ver o crear etiquetas      | ✅ Sí          |
| `/swagger/`        | GET        | Documentación Swagger      | ❌ No requiere |
| `/redoc/`          | GET        | Documentación Redoc        | ❌ No requiere |

---

### Ejemplo de Registro (POST `/api/register/`)

```json
{
  "username": "usuario",
  "email": "usuario@example.com",
  "password": "1234"
}
```

✅ Respuesta esperada:

```json
{
  "id": 3,
  "username": "usuario",
  "email": "usuario@example.com"
}
```

---

## 🔐 Autenticación

Para realizar peticiones a la API (crear posts, blogs, tags), es necesario autenticarse:

1. Ir a `/api-auth/login/`
2. Iniciar sesión con un usuario existente
3. Desde ahí, acceder a `/api/posts/`, `/api/blogs/`, etc.

---

## 🧑‍💻 Panel de Administración

Acceso al panel administrativo:

👉 [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
Usuario: *superuser* creado en el paso 5

Desde el admin se puede:

* Crear/editar blogs, posts y etiquetas
* Editar contenido con **TinyMCE**
* Exportar datos con **django-import-export**

---

## 📘 Documentación de la API

Cómo probar con Postman

1. Registrar usuario
POST http://127.0.0.1:8000/api/register/

2. Autenticarse
En cada petición → pestaña Authorization → Basic Auth
Usar usuario y contraseña creados.

3. Crear post
POST /api/posts/

{
  "title": "Primer post",
  "content": "Contenido del post"
}

---

## 📘 Documentación de la API

* **Swagger UI:** [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
* **Redoc UI:** [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

Ambas interfaces permiten probar los endpoints directamente desde el navegador.

---

## 🧾 Estructura del Proyecto

```
blog/
├── blog/                  # Configuración del proyecto
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│   └── asgi.py
├── blog_app/              # Aplicación principal
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── api.py
│   ├── admin.py
│   ├── urls.py
│   └── views.py
│   └── permissions.py
├── blog_app/            # tests unitarios
│   ├── __init__.py
│   └── factories.py
│   └── test_api.py
│   └── test_models.py
├── manage.py
├── pytest.py
└── requirements.txt
```

---
