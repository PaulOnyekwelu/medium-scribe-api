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

ALLOWED_HOSTS = ["localhost", "0.0.0.0"]

CSRF_TRUSTED_ORIGIN = ["http://localhost:8080"]


EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "support@paulonyekwelu.com"
DOMAIN = env("DOMAIN")
SITE_NAME = env("APP_NAME")
