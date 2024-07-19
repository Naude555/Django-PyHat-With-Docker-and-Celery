import os
from .base_settings import *
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:1337"
]  # TODO Change this if Nginx port is changed

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DEFAULT_SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("DEFAULT_SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("DEFAULT_SQL_USER", "user"),
        "PASSWORD": os.environ.get("DEFAULT_SQL_PASSWORD", "password"),
        "HOST": os.environ.get("DEFAULT_SQL_HOST", "localhost"),
        "PORT": os.environ.get("DEFAULT_SQL_PORT", "5432"),
    }
}
