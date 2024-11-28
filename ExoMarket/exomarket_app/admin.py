from django.contrib import admin
from .models import CustomUser, Item, Cart, CartItem

admin.site.register(CustomUser)
admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(CartItem)
