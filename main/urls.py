from django.urls import path
from .views import index, not_found

urlpatterns = [
    path('', index, name="index"),
    path('404', not_found),
]