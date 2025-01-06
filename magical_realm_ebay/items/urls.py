from django.urls import path
from .views import ItemListView, ItemDetailView, AddItemView

urlpatterns = [
    path("", ItemListView.as_view(), name="item_list"),
    path("<int:pk>/", ItemDetailView.as_view(), name="item_detail"),
    path("create/", AddItemView.as_view(), name="item_create"),
]
