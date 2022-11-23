from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from common.forms import UserForm,LocationForm
from common.models import Location,BarrierFreeInfo
from config import settings
import datetime
from ipware.ip import get_client_ip


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def location_check(request):
    address = request.GET.get('address')
    longitude = request.GET.get('longitude')
    latitude = request.GET.get('latitude')
    if(Location.objects.filter(address=address).exists()):
        return HttpResponse("found")
    else:
        context = {'address': address,'longitude':longitude,'latitude':latitude}
        return render(request, 'common/location_form.html',context)


def location_create(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            new_loc = form.save()
            new_loc.save()
            return redirect('restaurant:marker')
    else :
        return HttpResponse('GET')

def barrier_free_info_detail(request, barrier_free_info_id):
    barrier_free_info =get_object_or_404(BarrierFreeInfo,pk=barrier_free_info_id)
    context = {'barrier_free_info': barrier_free_info}
    return render(request, 'common/barrier_detail.html',context)



