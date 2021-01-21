from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import ItemSerializer
from .permissions import UserPermission
from ..models import Item


class ItemViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    lookup_field = "name"
    permission_classes = (UserPermission,)

    kwargs = {
        "url": {"view_name": "api:item-detail", "lookup_field": "name"}
    }

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(id=self.request.item.id)
