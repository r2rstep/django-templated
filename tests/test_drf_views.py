import pytest
from django.test import RequestFactory

from django_templated.users.api.views import UserViewSet
from django_templated.users.models import User
from django_templated.items.api.views import ItemViewSet
from django_templated.items.models import Item

pytestmark = pytest.mark.django_db


class TestUserViewSet:
    def test_get_queryset(self, user: User, rf: RequestFactory):
        view = UserViewSet()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert user in view.get_queryset()

    def test_me(self, user: User, rf: RequestFactory):
        view = UserViewSet()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        response = view.me(request)

        assert response.data == {
            "username": user.username,
            "email": user.email,
            "name": user.name,
            "url": f"http://testserver/api/users/{user.username}/",
        }


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
