from django.urls import path
from .views import *

urlpatterns = [
    path('<str:username>', user_index, name="profile"),
    path('<str:username>/profile', get_profile, name="profile"),
    path('<str:username>/privacy', get_password, name="privacy"),
    path('<str:username>/contact', get_contact, name="contact"),
]
