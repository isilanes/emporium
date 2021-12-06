import requests

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import status


@login_required
def main(request):

    url = f"http://{request.get_host()}/api/leases/lease/"
    response = requests.get(url)

    data = []
    if response.status_code == status.HTTP_200_OK:
        data = response.json()

    context = {
        "banner": "Contratos",
        "data": data,
    }

    return render(request, "leases/main.html", context)
