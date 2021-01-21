import urllib.parse

import pytest
from django.urls import resolve, reverse

from django_templated.items.models import Item

pytestmark = pytest.mark.django_db


def test_item_detail(item: Item):
    assert (
        reverse("api:item-detail", kwargs={"name": item.name})
        == urllib.parse.quote(f"/api/items/{item.name}/")
    )
    assert resolve(f"/api/items/{item.name}/").view_name == "api:item-detail"


def test_item_list():
    assert reverse("api:item-list") == "/api/items/"
    assert resolve("/api/items/").view_name == "api:item-list"
