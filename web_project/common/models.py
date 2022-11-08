from django.db import models
from config import settings
from datetime import datetime
import os
from uuid import uuid4
# Create your models here.
def get_file_path(instance, filename):
    ymd_path = datetime.now().strftime('%Y/%m/%d')
    ext = os.path.splitext(filename)[-1].lower()
    uuid_name = uuid4().hex
    return '/'.join(['common/', ymd_path, uuid_name+ext])

class Location(models.Model):
    name = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()
    address = models.CharField(max_length=200)

class BarrierFreeInfo(models.Model):
    elevator_count = models.IntegerField(null=True)
    elevator_detail = models.TextField(null=True)
    elevator_img = models.ImageField(null=True , upload_to=get_file_path)

    entrance_form = models.CharField(max_length=200)
    entrance_ramp = models.CharField(max_length=200)
    entrance_braille = models.BooleanField(null=True)
    entrance_detail = models.TextField(blank=True)
    entrance_img = models.ImageField(null=True , upload_to=get_file_path)

    restroom_floor = models.IntegerField(null=True)
    restroom_detail = models.TextField(blank=True)
    restroom_image = models.ImageField(null=True , upload_to=get_file_path)

    parking_count = models.IntegerField(null=True)
    parking_detail = models.TextField(blank=True)
    parking_img = models.ImageField(null=True , upload_to=get_file_path)

    def delete(self, *args, **kwargs):
        super(BarrierFreeInfo, self).delete(*args, **kwargs)
        os.remove(os.path.join(settings.MEDIA_ROOT, self.elevator_img.path))
        os.remove(os.path.join(settings.MEDIA_ROOT, self.entrance_img.path))
        os.remove(os.path.join(settings.MEDIA_ROOT, self.restroom_image.path))
        os.remove(os.path.join(settings.MEDIA_ROOT, self.parking_img.path))


