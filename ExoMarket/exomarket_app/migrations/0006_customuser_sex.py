# Generated by Django 5.1.3 on 2024-12-10 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "exomarket_app",
            "0005_item_quantity_item_rarity_alter_customuser_location_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="sex",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female")], default="F", max_length=10
            ),
            preserve_default=False,
        ),
    ]