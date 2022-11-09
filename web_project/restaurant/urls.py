from django.urls import path

from. import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:restaurant_id>/', views.detail, name='detail'),
]