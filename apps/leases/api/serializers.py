from rest_framework import serializers

from apps.leases.models import Lease
from apps.garage.api.serializers import GarageSerializer
from apps.people.api.serializers import PersonSerializer


class LeaseSerializer(serializers.ModelSerializer):
    resident = PersonSerializer(many=False)
    garage = GarageSerializer(many=False)

    class Meta:
        model = Lease
        fields = (
            "id",
            "resident",
            "start_date",
            "end_date",
            "garage",
        )
