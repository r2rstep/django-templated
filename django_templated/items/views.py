from django.contrib import messages
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView

from .models import Item


class ItemDetailView(DetailView):

    model = Item
    slug_field = "name"
    slug_url_kwarg = "name"


item_detail_view = ItemDetailView.as_view()


class ItemUpdateView(UpdateView):

    model = Item
    fields = ["name"]

    def get_success_url(self):
        return reverse("items:detail", kwargs={"name": self.request.item.name})

    def get_object(self):
        return Item.objects.get(name=self.request.item.name)

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


item_update_view = ItemUpdateView.as_view()
