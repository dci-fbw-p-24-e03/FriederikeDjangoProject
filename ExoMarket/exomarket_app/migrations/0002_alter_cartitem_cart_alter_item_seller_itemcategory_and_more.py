# Generated by Django 5.1.3 on 2024-11-28 14:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exomarket_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartitem",
            name="cart",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cart_items",
                to="exomarket_app.cart",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="seller",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items_to_sell",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
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
                        to="exomarket_app.itemcategory",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.AlterField(
            model_name="item",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="exomarket_app.itemcategory",
            ),
        ),
    ]