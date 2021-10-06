from django.db import models


class RealEstate(models.Model):
    """A Real-estate agency."""

    name = models.CharField('Name', max_length=100)

    def __str__(self):
        return self.name
