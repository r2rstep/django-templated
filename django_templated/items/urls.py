from django.urls import path

from django_templated.items.views import (
    item_detail_view,
    item_update_view,
)

app_name = "items"
urlpatterns = [
    path("~update/", view=item_update_view, name="update"),
    path("<str:username>/", view=item_detail_view, name="detail"),
]
