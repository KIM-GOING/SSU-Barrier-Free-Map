from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'base.html')

def test(request):
    return HttpResponse("test")

def map(request):
    return render(request,'test/map.html')