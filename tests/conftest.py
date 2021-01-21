import pytest

from django_templated.users.models import User
from django_templated.items.models import Item
from tests.factories import UserFactory, ItemFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def item() -> Item:
    return ItemFactory()
