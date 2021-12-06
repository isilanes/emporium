from django.db import models

from apps.garage.models import Garage
from apps.people.models import Person


class Lease(models.Model):
    """
    A Lease on a parking slot.
    """
    resident = models.ForeignKey(Person, on_delete=models.CASCADE, null=False)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE, null=False)

