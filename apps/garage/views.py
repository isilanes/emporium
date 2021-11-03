import requests

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import status

from .models import Garage


@login_required
def main(request):

    url = f"http://{request.get_host()}/api/garage/garage/"
    response = requests.get(url)

    data = []
    if response.status_code == status.HTTP_200_OK:
        data = response.json()

    data = sorted([(d.get("net_yearly_revenue_percent", 0), d.get("id"), d) for d in data], reverse=True)
    data = [d for (_, _, d) in data]

    context = {
        "banner": "Garajes",
        "data": data,
    }

    return render(request, "garage/main.html", context)
