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



class BarrierFreeInfo(models.Model):
    is_elevator = models.BooleanField(null=True)
    elevator_img = models.ImageField(null=True , upload_to=get_file_path)

    is_ramp = models.BooleanField(null=True)
    is_braille = models.BooleanField(null=True)
    entrance_img = models.ImageField(null=True , upload_to=get_file_path)

    is_accessible_toilet = models.BooleanField(null=True)
    toilet_img = models.ImageField(null=True , upload_to=get_file_path)

    parking_count = models.IntegerField(null=True)
    parking_img = models.ImageField(null=True , upload_to=get_file_path)

    detail = models.TextField(null=True)
    def delete(self, *args, **kwargs):
        super(BarrierFreeInfo, self).delete(*args, **kwargs)
        os.remove(os.path.join(settings.MEDIA_ROOT, self.elevator_img.path))
        os.remove(os.path.join(settings.MEDIA_ROOT, self.entrance_img.path))
        os.remove(os.path.join(settings.MEDIA_ROOT, self.toilet_img.path))
        os.remove(os.path.join(settings.MEDIA_ROOT, self.parking_img.path))

class Location(models.Model):
    name = models.CharField(max_length=200)
    longitude = models.FloatField()
    latitude = models.FloatField()
    address = models.CharField(max_length=200)
    barrier_free_info = models.ForeignKey(BarrierFreeInfo, on_delete=models.SET_NULL, null=True)

class Reply(models.Model):
    ip = models.CharField(max_length=20,null=True)
    text = models.TextField(null=True)
    createdate = models.DateTimeField(null=True)
    barrier_free_info = models.ForeignKey(BarrierFreeInfo, on_delete=models.CASCADE,null=True)