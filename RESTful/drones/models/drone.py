from django.db import models


class Drone(models.Model):
    name = models.CharField(max_length=250)
    drone_category = models.ForeignKey(
        'drones.DroneCategory',
        on_delete=models.CASCADE)
    manufacturing_date = models.DateTimeField()
    has_it_competed = models.BooleanField(default=False)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name