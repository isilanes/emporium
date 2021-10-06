from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Garage


@login_required
def main(request):

    garages = Garage.objects.all()

    context = {
        "garages": garages,
    }

    return render(request, "garage/main.html", context)
