from django.shortcuts import render
from main.models import House

# Create your views here.


def index(request):
    return render(request, 'index.html', {'name': 'rezz@_@'})


def house(request):
    houses = House.objects.all()
    return render(request, 'house/base.html', {'houses': houses})


def house_detail(request, house_id):
    house_by_id = House.objects.get(house_id=house_id)
    return render(request, 'house/house_detail.html', {'house': house_by_id})


def not_found(request):
    return render(request, '404.html')

