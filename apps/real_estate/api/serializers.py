from rest_framework import serializers

from apps.real_estate.models import RealEstate


class RealEstateSerializer(serializers.ModelSerializer):

    class Meta:
        model = RealEstate
        fields = (
            "id",
            "name",
        )
