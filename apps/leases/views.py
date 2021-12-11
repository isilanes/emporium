import requests

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from rest_framework import status

from apps.leases.models import Lease


def get_api_data(request, endpoint: str) -> list:
    url = f"http://{request.get_host()}/api/{endpoint}"
    response = requests.get(url)

    if response.status_code == status.HTTP_404_NOT_FOUND:
        raise Http404

    if response.status_code == status.HTTP_200_OK:
        return response.json()


@login_required
def main(request):

    endpoint = "leases/lease"
    data = get_api_data(request, endpoint)

    templates = []
    endpoint = "leases/lease-templates"
    for template in get_api_data(request, endpoint):
        templates.append((template.get("id"), template.get("comment")))

    people = []
    endpoint = "people/person"
    for person in get_api_data(request, endpoint):
        people.append((person.get("id"), person.get("name")))

    context = {
        "banner": "Contratos",
        "leases_active": True,
        "data": data,
        "ongoing": Lease.STATUS_ONGOING,
        "templates": templates,
        "people": people,
    }

    return render(request, "leases/main.html", context)
