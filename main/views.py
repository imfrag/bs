from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html', {'name': 'rezz@_@'})


def not_found(request):
    return render(request, '404.html')

