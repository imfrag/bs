from django.urls import path
from .views import *

urlpatterns = [
    path('<str:username>/', user_index, name="profile"),
    path('<str:username>/privacy', user_privacy, name="privacy"),
    path('<str:username>/contact', get_contact, name="contact"),

    path('<str:username>/billboard', get_billboard, name="billboard"),
    path('<str:username>/repair', get_repair, name="repair"),
    path('<str:username>/bill', get_bill, name="bill"),

    path('<str:username>/update/profile',
         update_profile,
         name="update_profile"),
]
