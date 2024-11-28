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


class Item(models.Model):
    CATEGORY_CHOICES = [
        ("armor", "Armor"),
        ("weapons", "Weapons"),
        ("ammunition", "Ammunition"),
        ("accessory", "Accessory"),
    ]
    # ARMOR_CHOICES = [
    #     ("barmor", "Body Armor"),
    #     ("belt", "Belt"),
    #     ("boot", "Boot"),
    #     ("glove", "Glove"),
    #     ("helm", "Helm"),
    #     ("shield", "Shield"),
    # ]
    # WEAPON_CHOICES = [
    #     ("axe", "Axe"),
    #     ("bow", "Bow"),
    #     ("crossbow", "Crossbow"),
    #     ("dagger", "Dagger"),
    #     ("spear", "Spear"),
    #     ("sword", "Sword"),
    #     ("wand", "Wand"),
    # ]
    # AMMUNITION_CHOICES = [("arrow", "Arrow"), ("bolt", "Bolt")]
    # ACCESSORY_CHOICES = [
    #     ("amulet", "Amulet"),
    #     ("charm", "Charm"),
    #     ("gem", "Gem"),
    #     ("jewel", "Jewel"),
    #     ("key", "Key"),
    #     ("potion", "Potion"),
    #     ("ring", "Ring"),
    #     ("rune", "Rune"),
    #     ("scroll", "Scroll"),
    # ]
    item_name = models.CharField(max_length=25)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    # armor_subcategory = models.CharField(
    #     choices=ARMOR_CHOICES, max_length=20, blank=True
    # )
    # weapon_subcategory = models.CharField(
    #     choices=WEAPON_CHOICES, max_length=20, blank=True
    # )
    # ammunition_subcategory = models.CharField(
    #     choices=AMMUNITION_CHOICES, max_length=20, blank=True
    # )
    # accessory_subcategory = models.CharField(
    #     choices=ACCESSORY_CHOICES, max_length=20, blank=True
    # )
    price = models.FloatField()
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="item_image/", blank=True)

    def __str__(self) -> str:
        return self.item_name


class Cart(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="cart"
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Cart of {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="items"
    )
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="cart_items"
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return f"{self.quantity} x {self.item.item_name} in {self.cart.user.username}'s cart"

    def total_price(self):
        return self.quantity * self.price
