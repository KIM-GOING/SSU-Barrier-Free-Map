from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('check/', views.location_check, name='location_check'),
    path('detail/<int:barrier_free_info_id>',views.barrier_free_info_detail, name='barrier_free_info_detail'),
    path('location/create',views.location_create,name='location_create'),
    path('reply/create/<int:barrier_free_info_id>',views.reply_create,name='reply_create'),
    path('bookmark/', views.bookmark, name='bookmark'),
    path('servicenotready/', views.service_not_ready, name='service_not_ready')
]