from rest_framework import viewsets, permissions

from apps.garage.api.serializers import GarageSerializer
from apps.garage.models import Garage


class GarageViewSet(viewsets.ModelViewSet):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
