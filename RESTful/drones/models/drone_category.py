from django.db import models


class DroneCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        app_label = 'drones'

    def __str__(self):
        return self.name
