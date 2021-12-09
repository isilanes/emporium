import requests

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from rest_framework import status

from apps.leases.models import Lease


def get_api_data(url: str) -> list:
    response = requests.get(url)

    if response.status_code == status.HTTP_404_NOT_FOUND:
        raise Http404

    if response.status_code == status.HTTP_200_OK:
        return response.json()


@login_required
def main(request):

    # data = []
    url = f"http://{request.get_host()}/api/leases/lease"
    data = get_api_data(url)

    templates = []
    url = f"http://{request.get_host()}/api/leases/lease-templates"
    for template in get_api_data(url):
        templates.append((template.get("id"), template.get("comment")))

    context = {
        "banner": "Contratos",
        "leases_active": True,
        "data": data,
        "ongoing": Lease.STATUS_ONGOING,
        "templates": templates,
    }

    return render(request, "leases/main.html", context)
