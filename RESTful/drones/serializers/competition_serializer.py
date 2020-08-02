from rest_framework import serializers

from ..models import Competition
from .drone_serializer import DroneSerializer


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    drone = DroneSerializer()

    class Meta:
        model = Competition
        fields = (
            'url',
            'pk',
            'distance_in_feet',
            'distance_achievement_date',
            'drone',
        )
