from django.db import models

from emporium import settings
from apps.tax.models import Tax


class Garage(models.Model):
    address = models.CharField('Address', max_length=100)
    number = models.CharField('Number', max_length=50)
    url = models.URLField(blank=True, null=True)
    asking_price = models.FloatField(blank=True, null=True)
    purchase_price = models.FloatField(blank=True, null=True)
    purchase_tax = models.ForeignKey(
        Tax,
        on_delete=models.SET_NULL,
        null=True,
        related_name="+",
    )
    rent_tax = models.ForeignKey(
        Tax,
        on_delete=models.SET_NULL,
        null=True,
        related_name="+",
    )
    expected_rent = models.FloatField(blank=True, null=True, default=0)
    actual_rent = models.FloatField(blank=True, null=True, default=0)
    width = models.FloatField(blank=True, null=True, default=0)
    length = models.FloatField(blank=True, null=True, default=0)
    community = models.FloatField(blank=True, null=True, default=0)
    ibi = models.FloatField(blank=True, null=True, default=0)

    @property
    def purchase_taxes(self) -> float:
        return self.purchase_tax.percent * self.purchase_price / 100.

    @property
    def net_sale_cost(self) -> float:
        return self.purchase_price + settings.NOTARY_FEE + self.purchase_taxes

    @property
    def monthly_rent_taxes(self) -> float:
        rent = self.actual_rent or self.expected_rent
        taxes = self.rent_tax.percent

        return rent * (1. - 1./(1. + taxes/100.))

    @property
    def yearly_expenses(self) -> float:
        return settings.YEARLY_AGENCY_FEE + self.community + self.ibi + 12 * self.monthly_rent_taxes

    @property
    def net_yearly_revenue(self):
        rent = self.actual_rent or self.expected_rent

        return 12. * rent - self.yearly_expenses

    @property
    def net_yearly_revenue_percent(self) -> float:
        return 100. * self.net_yearly_revenue / self.net_sale_cost

    def __str__(self) -> str:
        return f"{self.address}: {self.number}"
