from django.urls import path, include
from dj_rest_auth.views import PasswordResetConfirmView
from .views import CustomUserDetailsView


urlpatterns = [
    # it is important to keep the user/ route or any other custom route
    # at the top of the list. This is because some of the third party packages
    # may have the same route which will take precedence if kept on the top
    path("user/", CustomUserDetailsView.as_view(), name="user_details"),
    path("", include("dj_rest_auth.urls")),
    path("registration/", include("dj_rest_auth.registration.urls")),
    path(
        "password/reset/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]
