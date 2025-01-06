from django.urls import path
from .views import homepage, search_items, category_view

urlpatterns = [
    path("", homepage, name="marketplace_homepage"),
    path("search/", search_items, name="search_items"),
    path(
        "category/<slug:category_slug>/", category_view, name="category_view"
    ),
]
