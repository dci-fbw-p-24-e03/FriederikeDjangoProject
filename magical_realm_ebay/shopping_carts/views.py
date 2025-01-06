from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Cart, CartItem

from items.models import Item


@login_required
def add_to_cart(request, item_id):
    """Add an item to the user's shopping cart."""
    print("add_to_cart view called")  # Log when the view is accessed
    item = get_object_or_404(Item, id=item_id)
    print(f"Item retrieved: {item.item_name} (ID: {item.id})")

    if item.quantity < 1:
        messages.error(request, f"Sorry, {item.item_name} is out of stock.")
        print(f"Item {item.item_name} is out of stock.")
        return redirect("item_list")

    # Get or create the user's cart
    cart, created = Cart.objects.get_or_create(user=request.user)
    print(
        f"Cart {'created' if created else 'retrieved'} for user: {request.user.username}"
    )

    # Check if the item is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
    if not created:
        # If the item is already in the cart, increment the quantity
        cart_item.quantity += 1
    cart_item.save()
    print(
        f"CartItem {'created' if created else 'updated'}: {cart_item.item.item_name}, Quantity: {cart_item.quantity}"
    )

    messages.success(request, f"{item.item_name} has been added to your cart.")
    return redirect(request.META.get("HTTP_REFERER", "marketplace_homepage"))


@login_required
def view_cart(request):
    """Show the items in the user's shopping cart."""
    cart = Cart.objects.filter(user=request.user).first()
    if not cart:
        # If no cart exists, show an empty cart page
        return render(request, "shopping_carts/cart.html", {"cart_items": []})

    cart_items = cart.cart.all()
    return render(
        request, "shopping_carts/cart.html", {"cart_items": cart_items}
    )


@login_required
def purchase_cart(request):
    """Handle the purchase of all items in the user's shopping cart."""
    cart = Cart.objects.filter(user=request.user).first()

    if not cart or not cart.cart.exists():
        messages.error(request, "Your cart is empty. Nothing to purchase!")
        return redirect("view_cart")

    if request.method == "POST":
        # Remove all items in the cart
        cart.cart.all().delete()

        # Optionally delete the cart
        cart.delete()

        # Notify user of successful purchase
        messages.success(request, "Purchase successful! Thank you for shopping.")
        return redirect("marketplace_homepage")

    # If GET request, render a confirmation page
    return render(request, "shopping_carts/confirm_purchase.html", {"cart": cart})


@login_required
def remove_from_cart(request, cart_item_id):
    """Remove an item from the user's shopping cart."""
    cart_item = get_object_or_404(
        CartItem, id=cart_item_id, cart__user=request.user
    )
    cart_item.delete()
    messages.success(
        request, f"{cart_item.item.item_name} was removed from your cart."
    )
    return redirect(request.META.get("HTTP_REFERER", "view_cart"))
