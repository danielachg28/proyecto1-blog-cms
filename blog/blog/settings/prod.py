import os

import dj_database_url  # pyright: ignore[reportMissingImports]

from .base import *  # IMPORTANTE: trae ROOT_URLCONF, INSTALLED_APPS, MIDDLEWARE, etc.  # noqa: F403, F405


DEBUG = os.getenv("DJANGO_DEBUG", "False").lower() == "true"

# ALLOWED_HOSTS
ALLOWED_HOSTS_ENV = os.getenv("DJANGO_ALLOWED_HOSTS")
if ALLOWED_HOSTS_ENV:
    ALLOWED_HOSTS = [h.strip() for h in ALLOWED_HOSTS_ENV.split(",")]
else:
    raise Exception("ALLOWED_HOSTS no definido en producción!")

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
if DATABASE_URL is None:
    raise Exception("DATABASE_URL no definido en producción!")

DATABASES = {"default": dj_database_url.parse(DATABASE_URL, conn_max_age=600)}

# Opcional: seguridad extra en producción
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"
