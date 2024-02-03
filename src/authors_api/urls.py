import sys
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from .settings.base import env

APP_TITLE = env("APP_TITLE", default="Example API")
APP_DESC = env("APP_DESCRIPTION", default="API endpoints for the Example App")
DEVELOPER_EMAIL = env("DEVELOPER_EMAIL", default="example@gmail.com")

schema_view = get_schema_view(
    openapi.Info(
        title=APP_TITLE,
        default_version="v1",
        description=APP_DESC,
        contact=openapi.Contact(email=DEVELOPER_EMAIL),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(settings.ADMIN_URL, admin.site.urls),
]

admin.site.site_header = f"{APP_TITLE} Admin"
admin.site.site_title = f"{APP_TITLE} Admin Portal"
admin.site.index_title = f"Welcome to {APP_TITLE} Portal"
