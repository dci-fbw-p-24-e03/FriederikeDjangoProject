from django.urls import path
from . import views
from .views import ItemsListView, UserProfileView

app_name = "exomarket"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("marketplace/", ItemsListView.as_view(), name="marketplace"),
    path(
        "profile/<slug:username>",
        UserProfileView.as_view(),
        name="user-profile",
    ),
]
