from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta


def validate_user_age(value):
    """
    Validator for calculating user age.
    User must be 18 years old or older to register to the ExoMarket.
    Age is calculated as follows:
        current year - year of birth - 1(user's birthday hasn't been in current year yet = true) or 0 (user's brithday has already been in current year)
    and
    """
    today = timezone.now().date()
    age = (
        today.year
        - value.year
        - ((today.month, today.day) < (value.month, value.day))
    )
    if age < 18:
        raise ValidationError("You must be at least 18 years old to register.")
