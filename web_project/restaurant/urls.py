from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'restaurant'

urlpatterns = [
    path('', views.marker, name='marker'),
    path('check/',views.location_check, name='location_check')
]