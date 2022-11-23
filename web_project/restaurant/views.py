from django.shortcuts import render, redirect, get_object_or_404

from restaurant.models import *

# Create your views here.

def index(request) :
    restaurant_name = Restaurant.objects.order_by('-restaurant_name')
    context = {'restaurant':restaurant_name}
    return render(request, 'restaurant/restaurant_map.html', context)

def detail(request, restaurant_id) :
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    context = {'restaurant': restaurant}
    return render(request, 'restaurant/restaurant_detail.html', context)

def fix(request, restaurant_id) :
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    context = {'restaurant': restaurant}
    return render(request, 'restaurant/restaurant_fix.html', context)