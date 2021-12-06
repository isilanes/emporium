from django.db import models

from apps.garage.models import Garage
from apps.people.models import Person


class Lease(models.Model):
    """
    A Lease on a parking slot.
    """
    STATUS_FUTURE = 0
    STATUS_ONGOING = 1
    STATUS_FINISHED = 2

    resident = models.ForeignKey(Person, on_delete=models.CASCADE, null=False)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.resident} @ {self.garage}"
