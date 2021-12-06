from rest_framework import viewsets, permissions

from apps.leases.models import Lease
from apps.leases.api.serializers import LeaseSerializer


class LeasesViewSet(viewsets.ModelViewSet):
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
