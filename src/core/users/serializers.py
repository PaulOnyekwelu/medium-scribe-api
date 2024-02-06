from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.contrib.auth import get_user_model
from django_countries.serializer_fields import CountryField
from phonenumber_field.serializerfields import PhoneNumberField

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(source="profile.gender")
    city = serializers.CharField(source="profile.city")
    twitter_handle = serializers.CharField(source="profile.twitter_handle")
    profile_photo = serializers.ReadOnlyField(source="profile.profile_photo.url")
    phone_number = PhoneNumberField(source="profile.phone_number")
    country = CountryField(source="profile.country")

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "gender",
            "city",
            "country",
            "phone_number",
            "twitter_handle",
            "profile_photo",
        ]

    def to_representation(self, instance):
        """adds the admin field to the serialized data"""

        representation = super(UserSerializer, self).to_representation(instance)

        if instance.is_superuser:
            representation["admin"] = True

        return representation


class CustomRegisterSerializer(RegisterSerializer):
    username = None
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def get_cleaned_data(self):
        super().get_cleaned_data(self)

        return {
            "email": self.validated_data.get("email", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "password1": self.validated_data.get("password1", ""),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self)
        user.save()

        setup_user_email(request, user, email)

        user.email = self.cleaned_data.get("email")
        user.password = self.cleaned_data.get("password1")
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")

        return user
