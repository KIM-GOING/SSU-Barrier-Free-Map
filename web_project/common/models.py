from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()
    address = models.CharField(max_length=200)

class BarrierFreeInfo(models.Model):
    elevator_count = models.IntegerField(null=True)
    elevator_detail = models.TextField(null=True)
    elevator_img = models.ImageField(null=True)

    entrance_form = models.CharField(max_length=200)
    entrance_ramp = models.CharField(max_length=200)
    entrance_braille = models.BooleanField(null=True)
    entrance_detail = models.TextField(blank=True)
    entrance_img = models.ImageField(null=True)

    restroom_floor = models.IntegerField(null=True)
    restroom_detail = models.TextField(blank=True)
    restroom_image = models.ImageField(null=True)

    parking_count = models.IntegerField(null=True)
    parking_detail = models.TextField(blank=True)
    parking_img = models.ImageField(null=True)

