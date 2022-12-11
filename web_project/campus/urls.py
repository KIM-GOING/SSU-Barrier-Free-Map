from django.urls import path

from. import views

app_name = 'campus'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:campus_id>/', views.detail, name='detail')
]