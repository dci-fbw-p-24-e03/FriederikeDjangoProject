from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from profanity.validators import validate_is_profane
from .validators import validate_user_age


class CustomUser(AbstractUser):
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

    TOWN_CHOICES = {
        "RE": "Rogue Encampment",
        "LG": "Lut Gholein",
        "KD": "Kurast Docks",
        "PF": "Pandemonium Fortress",
        "HA": "Harrogath",
    }

    PHONE_VALIDATOR = [
        RegexValidator(
            regex=r"(\(?([\d \-\)\–\+\/\(]+){6,}\)?([ .\-–\/]?)([\d]+))",
            message=(
                "Enter a valid phone number. The phone number must:\n"
                "- Be at least 6 characters long\n"
                "- May include an optional country code, starting with '+'\n"
                "- Contain only digits, spaces, parentheses, dashes ('-'), slashes ('/'), or dots ('.')\n"
                "- Allow optional separators (spaces, dashes, or slashes) between sections\n"
                "- Be a sequence of valid characters that form a plausible number."
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
    location = models.CharField(
        choices=TOWN_CHOICES, max_length=25, blank=True
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        validators=PHONE_VALIDATOR,
    )
    sex = models.CharField(choices=SEX_CHOICES, max_length=10)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["username", "date_of_birth"],
                name="unique_username_birthday",
            )
        ]

    def __str__(self) -> str:
        return self.username


class ItemCategory(models.Model):
    cat_name = models.CharField(max_length=50, unique=True)  # cat=category
    parent_cat = models.ForeignKey(
        "ItemCategory",
        on_delete=models.CASCADE,
        null=True,  # NULL, if no parent_cat (if input is blank)
        blank=True,  # makes it optional (if blank, will be NULL in DB)
        related_name="item_category",
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        # show hierarchy, if exists
        if self.parent_cat:
            return f"{self.parent_cat.cat_name} -> {self.cat_name}"
        return self.cat_name


class Item(models.Model):
    RARITY_CHOICES = {
        "N": "Normal",
        "M": "Magic",
        "R": "Rare",
        "S": "Set",
        "U": "Unique",
    }
    item_name = models.CharField(max_length=25)
    category = models.ForeignKey(
        ItemCategory, on_delete=models.CASCADE, related_name="items"
    )
    price = models.FloatField()
    seller = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="items_to_sell"
    )
    creation_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(
        validators=[validate_is_profane],
        default=f"This is aitem of the category {category}",
    )
    image = models.ImageField(upload_to="item_images/", blank=True)
    quantity = models.IntegerField(null=True)
    rarity = models.CharField(
        choices=RARITY_CHOICES, max_length=10, blank=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["item_name", "category", "seller"],
                name="unique_itemname_category_seller",
            )
        ]

    def __str__(self) -> str:
        return self.item_name


class Cart(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="cart"
    )  # a user can have only one cart
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Cart of {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="cart_items"
    )  # a CartItem belongs to one Cart, but a Cart can contain multiple CartItems.
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="cart_items"
    )  # a CartItem represents one specific Item, but the same Item can appear in multiple CartItems
    quantity = models.PositiveIntegerField(default=1)
    price = models.FloatField(
        default=0.0
    )  # is set when creating the model CartItem

    def __str__(self) -> str:
        return f"{self.quantity} x {self.item.item_name} in cart"

    def total_price(self):
        return self.quantity * self.price

    def save(self, *args, **kwargs):
        if not self.pk:  # when creating a new CartItem
            self.price = (
                self.item.price
            )  # set the CartItem.price to the price of the Item it refers to
        super().save(*args, **kwargs)
