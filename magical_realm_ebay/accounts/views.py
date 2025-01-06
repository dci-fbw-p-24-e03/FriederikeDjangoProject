from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView

from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, CustomEditProfileForm


# class based views
class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    success_url = ""  # Redirect to marketplace after registration


class UserLogoutView(LogoutView):
    # template_name = "accounts/logout.html"
    success_url = "accounts/login.html"  # Redirect to login after registration


class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/register.html"
    success_url = ""  # Redirect to marketplace after registration


# function based views
@login_required
def user_profile(request):
    return render(request, "accounts/user_profile.html")


@login_required
def edit_profile(request):
    user = request.user
    if request.method == "POST":
        form = CustomEditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your profile has been updated successfully."
            )
            return redirect(
                "user_profile"
            )  # Redirect back to the profile page
    else:
        form = CustomEditProfileForm(instance=user)
    return render(request, "accounts/edit_profile.html", {"form": form})
