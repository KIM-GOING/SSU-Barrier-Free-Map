from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.core.paginator import  Paginator
from common.forms import UserForm,LocationForm,BarrierFreeInfoForm,ReplyForm
from common.models import Location,BarrierFreeInfo,Reply
from django.utils import timezone

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
    if (address == '서울 동작구 상도동 511'):
        return redirect('campus:index')

    if(Location.objects.filter(address=address).exists()):
        location = Location.objects.get(address=address)
        return redirect('common:barrier_free_info_detail',location.barrier_free_info.id)
    else:
        location_form = LocationForm()
        barrier_form = BarrierFreeInfoForm()
        context = {'address': address,'longitude':longitude,'latitude':latitude,
                   'barrier_form':barrier_form, 'location_form':location_form}
        return render(request, 'common/location_form.html',context)


def location_create(request):
    if request.method == 'POST':
        locform = LocationForm(request.POST)
        barrierform = BarrierFreeInfoForm(request.POST)
        if locform.is_valid():
            new_loc = locform.save(commit=False)

            new_barrier = BarrierFreeInfo()
            if request.POST['is_elevator']=='on':
                new_barrier.is_elevator = True
            else:
                new_barrier.is_elevator = False
            if request.POST['is_braille'] == 'on':
                new_barrier.is_braille = True
            else:
                new_barrier.is_braille = False
            if request.POST['is_ramp'] == 'on':
                new_barrier.is_ramp = True
            else:
                new_barrier.is_ramp = False
            if request.POST['is_accessible_toilet'] == 'on':
                new_barrier.is_accessible_toilet = True
            else:
                new_barrier.is_accessible_toilet = False

            new_barrier.elevator_img=request.FILES.get('elevator_img')
            new_barrier.toilet_img=request.FILES.get('toilet_img')
            new_barrier.entrance_img=request.FILES.get('entrance_img')
            new_barrier.parking_img = request.FILES.get('parking_img')
            new_barrier.parking_count=request.POST['parking_count']
            new_barrier.detail=request.POST['detail']

            new_barrier.save()
            new_loc.barrier_free_info = new_barrier
            new_loc.save()
            return redirect('restaurant:marker')
    else :
        return HttpResponse('GET')

def barrier_free_info_detail(request, barrier_free_info_id):
    barrier_free_info =get_object_or_404(BarrierFreeInfo,pk=barrier_free_info_id)
    reply_form = ReplyForm()

    context = {'barrier_free_info': barrier_free_info,'reply_form':reply_form}
    return render(request, 'common/barrier_detail.html',context)


def reply_create(request, barrier_free_info_id):
    barrier_free_info = get_object_or_404(BarrierFreeInfo,pk=barrier_free_info_id)
    if request.method=='POST':
        reply=Reply()
        reply.text = request.POST['text']
        reply.barrier_free_info = barrier_free_info
        reply.createdate = timezone.now()
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            reply.ip = x_forwarded_for.split(',')[0]
        else:
            reply.ip = request.META.get('REMOTE_ADDR')
        reply.save()
    return redirect('common:barrier_free_info_detail', barrier_free_info_id=barrier_free_info.id)

def index(request):
    return render(request,'common/middle.html')
