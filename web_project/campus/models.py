from django.db import models
from common.models import Location,BarrierFreeInfo
class Campus(models.Model):
    building_name = models.CharField(max_length=200)
    bottom_floor = models.IntegerField(null=True)
    top_floor = models.IntegerField(null=True)
    building_detail = models.TextField(null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    barrier_free_info = models.ForeignKey(BarrierFreeInfo, on_delete=models.CASCADE ,null=True)
