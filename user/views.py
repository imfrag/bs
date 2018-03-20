from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse

# Create your views here.


def user_index(request, username):
    data = render_to_string('user/profile.html', {'password': '123'})
    return render(request, 'user/base.html',
                  {'username': username,
                   'data': data})


def get_profile(request, username):
    data = render_to_string('user/profile.html', {'username': username})
    return JsonResponse({'data': data})


def get_password(request, username):
    data = render_to_string('404.html', {'password': '123'})
    return JsonResponse({'data': data})


def get_contact(request, username):
    print(request.is_ajax())
    data = render_to_string('user/contact.html')
    return JsonResponse({'data': data})
