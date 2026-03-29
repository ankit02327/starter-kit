from .base import *  # noqa: F403
from .base import STORAGES

SECRET_KEY = "ci-insecure-key-not-for-production"

DEBUG = True
ALLOWED_HOSTS = ["*"]

STORAGES["staticfiles"]["BACKEND"] = (
    "django.contrib.staticfiles.storage.StaticFilesStorage"
)

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
