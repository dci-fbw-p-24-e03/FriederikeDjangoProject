from django.db import models

from django.utils import timezone

from django.core.files.uploadedfile import InMemoryUploadedFile

import io

from PIL import Image

from profanity.validators import validate_is_profane

from accounts.models import CustomUserProfile

from django.utils.text import slugify


class ItemCategory(models.Model):
    cat_name = models.CharField(max_length=50, unique=True)  # cat=category
    parent_cat = models.ForeignKey(
        "ItemCategory",
        on_delete=models.CASCADE,
        null=True,  # NULL, if no parent_cat (if input is blank)
        blank=True,  # makes it optional (if blank, will be NULL in DB)
        related_name="item_category",
    )
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        # show hierarchy, if exists
        if self.parent_cat:
            return f"{self.parent_cat.cat_name} -> {self.cat_name}"
        return self.cat_name

    def save(self, *args, **kwargs):
        # Auto-generate slug from cat_name if not provided
        if not self.slug:
            self.slug = slugify(self.cat_name)
        super().save(*args, **kwargs)

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
    owner = models.ForeignKey(
        CustomUserProfile,
        on_delete=models.CASCADE,
        related_name="items_to_sell",
    )
    creation_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(
        validators=[validate_is_profane],
        default=f"This is an item of the category {category}",
    )
    image = models.ImageField(upload_to="item_images/", blank=True, null=True)
    quantity = models.IntegerField(null=True)
    rarity = models.CharField(
        choices=RARITY_CHOICES, max_length=10, blank=True
    )
    is_available = models.BooleanField(default=True)

    @property
    def days_online(self):
        """Compute how long the item has been online"""
        time_online = timezone.now() - self.creation_date
        return time_online.days

    def save(self, *args, **kwargs):
        """Automatically set is_available based on quantity."""
        self.is_available = self.quantity > 0

        """Resize item images before saving to the database."""
        if self.image:
            img = Image.open(self.image)
            img = img.convert(
                "RGB"
            )  # Convert to RGB to handle non-RGB formats
            img.thumbnail((300, 300))  # Resize to 300x300

            # Save resized image to a temporary buffer
            buffer = io.BytesIO()
            img.save(
                buffer, format="JPEG", quality=85
            )  # Save as JPEG with 85% quality
            buffer.seek(0)

            # Replace the image file with the resized version
            self.image = InMemoryUploadedFile(
                buffer,
                "ImageField",
                self.image.name,
                "image/jpeg",
                buffer.getbuffer().nbytes,
                None,
            )

        super().save(*args, **kwargs)

    # show the item_name when printing the object
    def __str__(self) -> str:
        return self.item_name
