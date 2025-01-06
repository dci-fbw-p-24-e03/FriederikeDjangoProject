from django.shortcuts import render, get_object_or_404

from items.models import Item, ItemCategory


# function-based views
def homepage(request):
    return render(request, "marketplace/homepage.html")


def search_items(request):
    query = request.GET.get("q", "")
    items = [item for item in Item.objects.all() if item.is_available]
    return render(
        request, "marketplace/search.html", {"query": query, "items": items}
    )


def category_view(request, category_slug):
    category = get_object_or_404(ItemCategory, slug=category_slug)
    items = Item.objects.filter(category=category, is_available=True)
    return render(
        request,
        "marketplace/category.html",
        {"category": category, "items": items},
    )
