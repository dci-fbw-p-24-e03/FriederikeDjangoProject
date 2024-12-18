from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import CustomLoginView, ItemsListView, UserProfileView

app_name = "exomarket"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("marketplace/", ItemsListView.as_view(), name="marketplace"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path(
        "logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"
    ),
    path(
        "profile/<slug:username>",
        UserProfileView.as_view(),
        name="user-profile",
    ),
]
