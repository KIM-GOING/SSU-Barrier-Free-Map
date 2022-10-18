from django.urls import path

from. import views

app_name = 'testapp'

urlpatterns = [
    path('', views.index,name='index'),
    path('test/', views.test, name='test'),
    path('map/', views.map, name='map')
]