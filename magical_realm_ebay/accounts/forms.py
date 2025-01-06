from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUserProfile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserProfile
        fields = [
            "username",
            "email",
            "date_of_birth",
            "profession",
            "phone_number",
            "sex",
        ]


class CustomEditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUserProfile
        fields = [
            "email",
            "profession",
            "phone_number",
            "sex",
            "date_of_birth",
        ]
        widgets = {
            "date_of_birth": forms.DateInput(
                attrs={"type": "date", "readonly": "readonly"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["date_of_birth"].disabled = (
            True  # Disable editing of date_of_birth
        )
