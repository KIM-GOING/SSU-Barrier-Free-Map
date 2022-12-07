from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse

from campus.models import *
# Create your views here.
def index(request):
    campus_list =Campus.objects.order_by('-building_name')
    context = {'campus_list' : campus_list}
    return render(request,'campus/campus_index.html',context)

def detail(request, name):
    return render(request,'campus/campus_details_'+name+'.html')

