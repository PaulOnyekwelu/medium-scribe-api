import os
from celery import Celery
from django.conf import settings
from .settings.base import env

#TODO: change in production
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "authors_api.settings.local")

app = Celery(env("APP_TITLE", default="example-api"))

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
