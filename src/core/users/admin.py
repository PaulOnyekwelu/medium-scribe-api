from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from .forms import UserChangeForm, UserCreationForm

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    form = UserChangeForm
    add_form = UserCreationForm
    model = User

    list_display = [
        "pkid",
        "id",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    ]

    list_display_links = ("pkid", "id", "email")

    list_filter = ["email", "is_staff", "is_active"]

    fieldsets = (
        (_("Login Credentials"), {"fields": ("email", "password")}),
        (_("Personal Information"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissons and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        None,
        {
            "classes": ("wide"),
            "fields": ("email", "first_name", "last_name", "password1", "password2"),
        },
    )
    search_fields = ["email", "first_name", "last_name"]


admin.site.register(User, UserAdmin)
