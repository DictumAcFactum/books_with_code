from rest_framework import serializers
from django.contrib.auth.models import User

from ..models import Drone


class UserDroneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drone
        fields = (
            'url',
            'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    drones = UserDroneSerializer(
        many=True,
        read_only=True,
        source='drones_set'
    )
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = (
            'url',
            'pk',
            'username',
            'drone',
            'owner',
        )
