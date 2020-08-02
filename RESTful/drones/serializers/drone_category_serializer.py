from rest_framework import serializers

from ..models import DroneCategory

class DroneCategorySerializer(serializers.Serializer):
    drones = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='drone-detail')

    class Meta:
        model = DroneCategory
        fields = (
            'url',
            'pk',
            'name',
            'drones',
        )