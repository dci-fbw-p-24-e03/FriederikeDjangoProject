# Generated by Django 5.1.4 on 2025-01-06 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuserprofile",
            name="sold_items_count",
            field=models.PositiveIntegerField(default=0),
        ),
    ]