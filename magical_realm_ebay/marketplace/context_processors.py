from items.models import ItemCategory


def categories_context(request):
    """Make categories available in all templates."""
    categories = ItemCategory.objects.all()
    return {"categories": categories}
