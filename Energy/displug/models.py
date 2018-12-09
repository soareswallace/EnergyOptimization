from django.db import models


class Devices(models.Model):
    def __str__(self):
        return self.name
    consumption = models.FloatField(default=0.0)
    average_consumption = models.FloatField(default=0.0)
    name = models.CharField(max_length=200)
    active = models.BooleanField(max_length=False)


class Sensors(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    connected = models.BooleanField(default=False)

