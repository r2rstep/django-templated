from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from django_templated.users.api.views import UserViewSet
from django_templated.items.api.views import ItemViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("items", ItemViewSet)


app_name = "api"
urlpatterns = router.urls
