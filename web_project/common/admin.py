from django.contrib import admin
from .models import *
from campus.models import Campus
from restaurant.models import Restaurant
# Register your models here.


admin.site.register(Location)
admin.site.register(BarrierFreeInfo)
admin.site.register(Restaurant)
admin.site.register(Campus)
admin.site.register(Reply)
