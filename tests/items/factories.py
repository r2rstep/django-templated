import random

from factory import Faker
from factory.django import DjangoModelFactory

from django_templated.items.models import Item


class ItemFactory(DjangoModelFactory):

    name = Faker("name")
    prop = random.randint(0, 100)

    class Meta:
        model = Item
