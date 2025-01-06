from django.db import models

from django.utils import timezone

from django.core.validators import RegexValidator

from django.contrib.auth.models import AbstractUser

from .validators import validate_user_age


class CustomUserProfile(AbstractUser):
    """
    A custom user model inheriting from the build-in AbstractUser.
    This model expands the AbstractUser by fields for sex, date of birth,
        phone number and profession.
    Date of birth is mandatory since a user has to be at least 18 years old
        (adult) to legally sell and buy items.

    required fields: username, password, date_of_birth
    other fields are optional.
    """

    SEX_CHOICES = {"M": "Male", "F": "Female"}

    PROFESSION_CHOICES = {
        "AM": "Amazon",
        "NE": "Necromancer",
        "BA": "Barbarian",
        "MA": "Mage",
        "PA": "Paladin",
        "AS": "Assassin",
        "DR": "Druid",
    }

    PHONE_VALIDATOR = [
        RegexValidator(
            regex=r"(\(?([\d \-\)\–\+\/\(]+){6,}\)?([ .\-–\/]?)([\d]+))",
            message=(
                "Enter a valid phone number:\n"
                "- Must be at least 6 characters long\n"
                "- May include an optional country code, starting with '+'\n"
                "- Must contain only digits, spaces, parentheses, dashes ('-'), slashes ('/'), or dots ('.')\n"
                "- Allows optional separators (spaces, dashes, or slashes) between sections\n"
                "- Must be a sequence of valid characters that form a plausible number."
            ),
        )
    ]

    date_of_birth = models.DateField(
        validators=[validate_user_age], default=timezone.now
    )

    profession = models.CharField(
        choices=PROFESSION_CHOICES,
        max_length=15,
        blank=True,
    )

    phone_number = models.CharField(
        max_length=20, validators=PHONE_VALIDATOR, blank=True
    )

    sex = models.CharField(choices=SEX_CHOICES, max_length=10, blank=True)

    sold_items_count = models.PositiveIntegerField(default=0)

    def increment_sold_items(self):
        """Increment the count of sold items."""
        self.sold_items_count += 1
        self.save()
