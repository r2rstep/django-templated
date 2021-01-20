from django.db.models import CharField, Model, IntegerField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Item(Model):
    """Default user for django-templated."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    prop = IntegerField()

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("items:detail", kwargs={"id": self.name})
