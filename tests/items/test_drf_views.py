import pytest
from django.test import RequestFactory

from django_templated.items.api.views import ItemViewSet
from django_templated.items.models import Item

pytestmark = pytest.mark.django_db


class TestItemViewSet:
    def test_get_queryset(self, item: Item, rf: RequestFactory):
        view = ItemViewSet()
        request = rf.get("/fake-url/")
        request.item = item

        view.request = request

        assert item in view.get_queryset()

    def test_retrieve(self, item: Item, rf: RequestFactory):
        request = rf.get("/fake-url/")
        request.item = item
        view = ItemViewSet.as_view({'get': 'retrieve'})

        response = view(request, name=item.name)

        assert response.data == {
            "name": item.name,
            "prop": item.prop,
        }
