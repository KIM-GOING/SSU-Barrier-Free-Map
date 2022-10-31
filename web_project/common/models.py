from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

class BarrierFreeInfo(models.Model):
    entrance = models.CharField(max_length=200)
    slope = models.CharField(max_length=200)
    is_accessible_toilet = models.BooleanField()
    is_braille = models.BooleanField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

