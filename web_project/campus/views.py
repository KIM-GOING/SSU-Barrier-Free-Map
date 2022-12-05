from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse

from campus.models import *
# Create your views here.
def index(request):
    campus_list =Campus.objects.order_by('-building_name')
    context = {'campus_list' : campus_list}
    return render(request,'campus/campus_index.html',context)

def detail(request,campus_id):
    campus = get_object_or_404(Campus, pk =campus_id)
    context = {'campus':campus}
    return render(request,'campus/campus_detail.html',context)

