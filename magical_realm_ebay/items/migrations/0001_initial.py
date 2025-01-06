# Generated by Django 5.1.4 on 2025-01-02 18:08

import django.db.models.deletion
import django.utils.timezone
import profanity.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ItemCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cat_name", models.CharField(max_length=50, unique=True)),
                (
                    "parent_cat",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="item_category",
                        to="items.itemcategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Category",
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item_name", models.CharField(max_length=25)),
                ("price", models.FloatField()),
                (
                    "creation_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "description",
                    models.TextField(
                        default="This is an item of the category <django.db.models.fields.related.ForeignKey>",
                        validators=[profanity.validators.validate_is_profane],
                    ),
                ),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="item_images/"),
                ),
                ("quantity", models.IntegerField(null=True)),
                (
                    "rarity",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("N", "Normal"),
                            ("M", "Magic"),
                            ("R", "Rare"),
                            ("S", "Set"),
                            ("U", "Unique"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items_to_sell",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="items.itemcategory",
                    ),
                ),
            ],
        ),
    ]
