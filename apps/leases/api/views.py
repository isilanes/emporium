import json

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status as http_status

from apps.leases.models import Lease, LeaseTemplate
from apps.leases.api.serializers import LeaseSerializer, LeaseTemplateSerializer


class LeasesViewSet(viewsets.ModelViewSet):
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    @action(detail=False, methods=("POST",), url_name="create-lease")
    def create_lease(self, request):
        payload = json.loads(request.POST.get("payload", ""))

        return Response(status=http_status.HTTP_201_CREATED)


class LeaseTemplatesViewSet(viewsets.ModelViewSet):
    queryset = LeaseTemplate.objects.all()
    serializer_class = LeaseTemplateSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
