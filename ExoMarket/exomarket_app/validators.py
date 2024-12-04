from django.core.exceptions import ValidationError


def validate_user_age(value):
    if value < 18:
        raise ValidationError("You must be of full age to register.")

