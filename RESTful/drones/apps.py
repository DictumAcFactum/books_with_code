from django.apps import AppConfig


class DronesConfig(AppConfig):
    name = 'drones'

    def ready(self):
        from drones.models import DroneCategory, Pilot, Drone