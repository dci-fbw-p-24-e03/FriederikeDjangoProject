from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView, TemplateView

from .models import CustomUser, Item


# class-based views
class CustomLoginView(LoginView):
    template_name = "exomarket_app/user_login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("marketplace")


class UserProfileView(DetailView):
    model = CustomUser
    template_name = "exomarket_app/user_profile.html"
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"


class ItemsListView(ListView):
    model = Item
    template_name = "exomarket_app/item_card.html"
    context_object_name = "items_list"


# function-based views
def home(request):
    return render(request, "exomarket_app/home.html")


def about(request):
    return HttpResponse("<h1>About the ExoMarket</h1>")
