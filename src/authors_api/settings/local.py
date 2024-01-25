import secrets
from .base import *  # noqa
from .base import env


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default=secrets.token_urlsafe(30),
)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []

CSRF_TRUSTED_ORIGIN = ["http://localhost:8080"]
