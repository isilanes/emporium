from rest_framework import viewsets, permissions

from apps.leases.models import Lease, LeaseTemplate
from apps.leases.api.serializers import LeaseSerializer, LeaseTemplateSerializer


class LeasesViewSet(viewsets.ModelViewSet):
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class LeaseTemplatesViewSet(viewsets.ModelViewSet):
    queryset = LeaseTemplate.objects.all()
    serializer_class = LeaseTemplateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
