from django.db import models

from django.utils import timezone

from items.models import Item

from accounts.models import CustomUserProfile


class Cart(models.Model):
    user = models.OneToOneField(
        CustomUserProfile, on_delete=models.CASCADE, related_name="cart"
    )  # a user can have only one cart
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Cart of {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="cart"
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
