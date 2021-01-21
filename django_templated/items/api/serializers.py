from rest_framework import serializers

from ..models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["name", "prop"]

        extra_kwargs = {
            "url": {"view_name": "api:item-detail", "lookup_field": "name"}
        }
