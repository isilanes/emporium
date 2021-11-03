from django.db import models


class Tax(models.Model):
    name = models.CharField('Name', max_length=50)
    percent = models.FloatField()

    @property
    def tax_fraction(self) -> float:
        """
        If I charge 1.00 euros, including Taxes (this one), what fraction
        of this euro is taxes.
        """
        return 1. - 1./(1. + self.percent/100.)

    def __str__(self):
        return self.name
