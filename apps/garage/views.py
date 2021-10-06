from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Garage


@login_required
def main(request):

    context = {}

    return render(request, "garage/main.html", context)
