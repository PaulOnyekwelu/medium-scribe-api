from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            raise ValueError(_("Please provide a valid email address"))

    def create_user(self, firstname, lastname, email, password, **extra_fields):
        if not firstname or not lastname or not email:
            raise ValueError(_("firstname, lastname, and email fields are required!"))

        email = self.normalize_email(email)
        self.email_validator(email)

        user = self.model(
            first_name=firstname, last_name=lastname, email=email, **extra_fields
        )

        user.set_password(password)

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        user.save(using=self._db)

        return user

    def create_superuser(self, firstname, lastname, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("SuperUser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("SuperUser must have is_superuser=True."))
        if extra_fields.get("is_active") is not True:
            raise ValueError(_("SuperUser must have is_active=True."))
        if not password:
            raise ValueError(_("Password field is required."))
        if not email:
            raise ValueError(_("Email field is required."))

        email = self.normalize_email(email)
        self.email_validator(email)

        user = self.create_user(firstname, lastname, email, password, **extra_fields)
        user.save(using=self._db)

        return user
