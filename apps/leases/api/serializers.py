from rest_framework import serializers

from apps.leases.models import Lease
from apps.garage.api.serializers import GarageSerializer
from apps.people.api.serializers import PersonSerializer


class LeaseSerializer(serializers.ModelSerializer):
    resident = PersonSerializer(many=False)
    garage = GarageSerializer(many=False)
    status = serializers.SerializerMethodField()

    class Meta:
        model = Lease
        fields = (
            "id",
            "resident",
            "start_date",
            "end_date",
            "garage",
            "status",
        )

    @staticmethod
    def get_status(obj: Lease) -> str:
        if not obj.start_date:
            return Lease.STATUS_FUTURE

        if not obj.end_date:
            return Lease.STATUS_ONGOING

        return Lease.STATUS_FINISHED
