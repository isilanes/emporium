import requests

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import status

from .models import Garage


@login_required
def main(request):

    url = f"http://{request.get_host()}/api/garage/garage/"
    response = requests.get(url)

    data = {}
    if response.status_code == status.HTTP_200_OK:
        data = response.json()

    context = {
        "banner": "Garajes",
        "data": data,
    }

    return render(request, "garage/main.html", context)
