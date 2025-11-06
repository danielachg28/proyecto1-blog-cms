import os

import dj_database_url  # pyright: ignore[reportMissingImports]

from .base import *  # IMPORTANTE: trae ROOT_URLCONF, INSTALLED_APPS, MIDDLEWARE, etc.  # noqa: F403, F405
from .base import BASE_DIR


DEBUG = os.getenv("DJANGO_DEBUG", "False").lower() == "true"

# ALLOWED_HOSTS
ALLOWED_HOSTS_ENV = os.getenv("DJANGO_ALLOWED_HOSTS")
if ALLOWED_HOSTS_ENV:
    ALLOWED_HOSTS = [host.strip() for host in ALLOWED_HOSTS_ENV.split(",")]
else:
    # Valor por defecto solo si quieres incluir subdominios de Railway
    ALLOWED_HOSTS = [
        "localhost",
        "127.0.0.1",
        ".railway.app",
        "proyecto1-blog-cms-dev-v1-version.railway.app",
    ]

# CSRF_TRUSTED_ORIGINS
CSRF_TRUSTED_ORIGINS = [
    "https://*.railway.app",  # *: Para incluir todos los subdominios de railway
]

# SECRET_KEY
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
if not SECRET_KEY:
    raise Exception("SECRET_KEY no definido en producción!")

# DATABASES
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    DATABASES = {"default": dj_database_url.parse(DATABASE_URL, conn_max_age=600)}
else:
    # fallback a SQLite si no hay DATABASE_URL
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Opcional: seguridad extra en producción
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"
