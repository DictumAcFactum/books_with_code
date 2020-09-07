from django.db import models


class Competition(models.Model):
    pilot = models.ForeignKey(
        'drones.Pilot',
        on_delete=models.CASCADE)
    drone = models.ForeignKey(
        'drones.Drone',
        on_delete=models.CASCADE)
    distance_in_feet = models.IntegerField()
    distance_achievement_date = models.DateTimeField()

    class Meta:
        ordering = ('-distance_in_feet',)
        app_label = 'drones'
