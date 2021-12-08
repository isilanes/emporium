import requests

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response

from apps.leases.models import Lease


@login_required
def main(request):

    url = f"http://{request.get_host()}/api/leases/lease"
    response = requests.get(url)

    data = []
    if response.status_code == status.HTTP_404_NOT_FOUND:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if response.status_code == status.HTTP_200_OK:
        data = response.json()

    context = {
        "banner": "Contratos",
        "leases_active": True,
        "data": data,
        "ongoing": Lease.STATUS_ONGOING,
    }

    return render(request, "leases/main.html", context)
