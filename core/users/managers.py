from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def validate_email(self, email):
        """validate user email address"""
        try:
            validate_email(email)
            return True
        except ValidationError as error:
            raise ValueError(_("Please Provide a valid Email Address"))

    def create_user(self, first_name, last_name, email, password, **extra_fields):
        """create and return a new user"""
        if not first_name:
            raise (_("first_name field required"))
        if not last_name:
            raise (_("last_name field required"))
        if not email:
            raise (_("email field required"))

        email = self.normalize_email(email)
        self.validate_email(email)

        user = self.model(
            first_name=first_name, last_name=last_name, email=email, **extra_fields
        )
        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, email, password, **extra_fields):
        """create and return a new super user"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is None:
            raise (_("Superuser must have is_staff=True"))
        if extra_fields.get("is_superuser") is None:
            raise (_("Superuser must have is_superuser=True"))
        if extra_fields.get("is_active") is None:
            raise (_("Superuser must have is_active=True"))
        if not password:
            raise (_("password field is required"))
        if not email:
            raise (_("Email field is required"))

        email = self.normalize_email(email)
        self.validate_email(email)

        user = self.create_user(first_name, last_name, email, password, **extra_fields)
        user.save(using=self._db)

        return user
