from django import forms
from .models import Item

class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "item_name",
            "category",
            "price",
            "description",
            "image",
            "quantity",
            "rarity",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }

