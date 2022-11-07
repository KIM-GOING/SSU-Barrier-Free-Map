from django.contrib import admin
from .models import *
from campus.models import Campus
from restaurant.models import Restaurant,Review
from testapp.models import TestImage
# Register your models here.


admin.site.register(Location)
admin.site.register(BarrierFreeInfo)
admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(Campus)
admin.site.register(TestImage)

