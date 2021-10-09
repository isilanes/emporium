from rest_framework import serializers

from apps.garage.models import Garage


class GarageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Garage
        fields = ("address", "number")
