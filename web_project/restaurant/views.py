from django.shortcuts import render,get_object_or_404,HttpResponse
from common.models import Location,BarrierFreeInfo
# Create your views here.
def marker(request):
        marker_list = Location.objects.order_by('id')
        context = {'marker_list': marker_list}
        return render(request, 'restaurant/00-orange-main.html', context)

def location_check(request):
    address = request.GET.get('address')
    longitude = request.GET.get('longitude')
    latitude = request.GET.get('latitude')
    if(Location.objects.filter(address=address).exists()):
        return HttpResponse("found")
    else:
        return HttpResponse(address + '|' + longitude + '|' + latitude)
