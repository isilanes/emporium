from rest_framework import serializers

from apps.garage.models import Garage
from apps.real_estate.api.serializers import RealEstateSerializer


class GarageSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source="parking.address", default=None)
    real_estate = RealEstateSerializer(many=False)
    price = serializers.SerializerMethodField()
    rent = serializers.SerializerMethodField()

    class Meta:
        model = Garage
        fields = (
            "id",
            "address",
            "number",
            "real_estate",
            "price",
            "rent",
            "net_yearly_revenue_percent",
        )

    @staticmethod
    def get_price(obj: Garage) -> float:
        return obj.purchase_price or obj.asking_price

    @staticmethod
    def get_rent(obj: Garage) -> float:
        return obj.actual_rent or obj.expected_rent
