import os

import dj_database_url  # pyright: ignore[reportMissingImports]

from .base import *  # IMPORTANTE: trae ROOT_URLCONF, INSTALLED_APPS, MIDDLEWARE, etc.  # noqa: F403, F405
from .base import BASE_DIR  # noqa: F401


# DEBUG
DEBUG = os.getenv("DJANGO_DEBUG", "True").lower() == "true"


# ALLOWED_HOSTS
# Si se define en el entorno, usa eso; si no, usa BaseConfig + localhost y 0.0.0.0
ALLOWED_HOSTS_ENV = os.getenv("DJANGO_ALLOWED_HOSTS")
if ALLOWED_HOSTS_ENV:
    ALLOWED_HOSTS = [h.strip() for h in ALLOWED_HOSTS_ENV.split(",")]
else:
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]


# DATABASES
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR / 'db.sqlite3'}")

if DATABASE_URL.startswith("sqlite"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",  # noqa: F405
        }
    }
else:  # Producción: PostgreSQL
    DATABASES = {"default": dj_database_url.parse(DATABASE_URL, conn_max_age=600)}
