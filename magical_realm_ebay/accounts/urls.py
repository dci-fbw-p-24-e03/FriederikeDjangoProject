from django.urls import path

from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
)
from .views import (
    user_profile,
    edit_profile,
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
)

urlpatterns = [
    path(
        "login/",
        UserLoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path(
        "logout/",
        UserLogoutView.as_view(next_page="/accounts/login/"),
        name="logout",
    ),
    path("register/", UserRegisterView.as_view(), name="register"),
    path("profile/", user_profile, name="user_profile"),
    path("edit-profile/", edit_profile, name="edit_profile"),
    path(
        "password-change/",
        PasswordChangeView.as_view(
            template_name="accounts/change_password.html",
            success_url="/accounts/password-change-done/",
        ),
        name="password_change",
    ),
    path(
        "password-change-done/",
        PasswordChangeDoneView.as_view(
            template_name="accounts/change_password_done.html"
        ),
        name="password_change_done",
    ),
]
