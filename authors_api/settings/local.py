import sys
from .base import *  # noqa
from .base import env


# sys.dont_write_bytecode = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="6xdzj7MCXVo0XSguXLlCGeOKLyGRHrzBqYuM_e0BCOvNfz_J1gA",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "support@paulonyekwelu.com"
DOMAIN = env("DOMAIN")
SITE_NAME = env("APP_NAME")
