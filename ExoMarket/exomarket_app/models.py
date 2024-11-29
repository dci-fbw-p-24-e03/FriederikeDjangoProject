from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    # SEX_CHOICES = [("M", "Male"), ("F", "Female")]
    PROFESSION_CHOICES = [
        ("amazon", "Amazon"),
        ("necromancer", "Necromancer"),
        ("barbarian", "Barbarian"),
        ("mage", "Mage"),
        ("paladin", "Paladin"),
        ("assassin", "Assassin"),
        ("druid", "Druid"),
    ]
    TOWN_CHOICES = [
        ("re", "Rogue Encampment"),
        ("lg", "Lut Gholein"),
        ("kd", "Kurast Docks"),
        ("pf", "Pandemonium Fortress"),
        ("ha", "Harrogath"),
    ]
    profession = models.CharField(
        choices=PROFESSION_CHOICES, max_length=15, blank=True
    )
    location = models.CharField(
        choices=TOWN_CHOICES, max_length=25, blank=True
    )
    phone_number = models.CharField(max_length=20, blank=True)
    # sex = models.CharField(choices=SEX_CHOICES, max_length=10)

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
        verbose_name_plural = "Categories"

    def __str__(self):
        # show hierarchy, if exists
        if self.parent_cat:
            return f"{self.parent_cat.cat_name} -> {self.cat_name}"
        return self.cat_name


class Item(models.Model):
    item_name = models.CharField(max_length=25)
    category = models.ForeignKey(
        ItemCategory, on_delete=models.CASCADE, related_name="items"
    )
    price = models.FloatField()
    seller = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="items_to_sell"
    )
    creation_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="item_image/", blank=True)

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
