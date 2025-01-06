from django.shortcuts import render

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView

from .models import Item

from .forms import AddItemForm


# class based views
class ItemListView(ListView):
    model = Item
    template_name = "items/item_list.html"
    context_object_name = "items"


class ItemDetailView(DetailView):
    model = Item
    template_name = "items/item_detail.html"


@method_decorator(login_required, name="dispatch")
class AddItemView(CreateView):
    model = Item
    form_class = AddItemForm
    template_name = "items/add_item.html"
    success_url = (
        "/user/profile/"  # Redirect to the user's profile upon success
    )

    def form_valid(self, form):
        # Attach the logged-in user as the owner of the item
        form.instance.owner = self.request.user
        messages.success(
            self.request, "Your item has been added successfully!"
        )
        return super().form_valid(form)
