from django import forms
from django.contrib.auth.forms import UserCreationForm
import datetime
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    User Creation Form for CustomUser model to expand the in-built form.
    """

    sex = forms.ChoiceField(
        choices=CustomUser.SEX_CHOICES,
        widget=forms.RadioSelect(attrs={"class": "form-check-input"}),
    )

    date_of_birth = forms.DateField(  # HTML5 DateField: creates a calender to chose the date from
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
            }
        ),
        help_text="Please select your date of birth. You must be at least 18 years old to register.",
    )

    phone_number = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Phone Number"}
        ),
        help_text="Enter a valid phone number. The phone number must:\n"
        "- Be at least 6 characters long\n"
        "- May include an optional country code, starting with '+'\n"
        "- Contain only digits, spaces, parentheses, dashes ('-'), slashes ('/'), or dots ('.')\n"
        "- Allow optional separators (spaces, dashes, or slashes) between sections\n"
        "- Be a sequence of valid characters that form a plausible number.",
    )

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "sex",
            "date_of_birth",
            "phone_number",
            "profession",
            "location",
        )
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Username"}
            ),
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Last Name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "profession": forms.Select(attrs={"class": "form-control"}),
            "location": forms.Select(attrs={"class": "form-control"}),
        }
