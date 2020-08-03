from rest_framework import serializers

from ..models import DroneCategory
from ..serializers import DroneSerializer

class DroneCategorySerializer(serializers.ModelSerializer):
    drones = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='drone-detail', source='drone_set')

    class Meta:
        model = DroneCategory
        fields = (
            'url',
            'pk',
            'name',
            'drones',
        )

    def create(self, validated_data):
        drone_serializer = DroneSerializer(data=validated_data.get('drones'))
        if drone_serializer.is_valid():
            drone_serializer.save()
        return DroneCategory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if validated_data.get('drones'):
            drone_serializer = DroneSerializer(data=validated_data.get('drones'))
            if drone_serializer.is_valid():
                drone_serializer.save()
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance