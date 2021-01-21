from django.db.models import CharField, Model, IntegerField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Item(Model):

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    prop = IntegerField()

    def get_absolute_url(self):
        return reverse("items:detail", kwargs={"name": self.name})
