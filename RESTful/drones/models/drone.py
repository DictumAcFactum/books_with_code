from django.db import models


class Drone(models.Model):
    name = models.CharField(max_length=250, unique=True)
    drone_category = models.ForeignKey(
        'drones.DroneCategory',
        on_delete=models.CASCADE)
    manufacturing_date = models.DateTimeField()
    has_it_competed = models.BooleanField(default=False)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        app_label = 'drones'

    def __str__(self):
        return self.name
