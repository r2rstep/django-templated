import pytest

from django_templated.items.models import Item
from tests.items.factories import ItemFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def item() -> Item:
    return ItemFactory()
