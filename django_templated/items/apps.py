from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ItemsConfig(AppConfig):
    name = "django_templated.items"
    verbose_name = _("Items")

    def ready(self):
        try:
            import django_templated.items.signals  # noqa F401
        except ImportError:
            pass
