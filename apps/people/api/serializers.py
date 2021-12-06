from rest_framework import serializers

from apps.people.models import Person


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = (
            "id",
            "title",
            "name",
            "status",
            "nationality",
            "address",
            "id_card",
            "email",
            "telephone",
        )
