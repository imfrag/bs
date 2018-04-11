from django.urls import path
from .views import index, house, house_detail, not_found

urlpatterns = [
    path('', index, name="index"),
    path('house', house, name="house"),
    path('house/<int:house_id>', house_detail, name="house_detail"),
    path('404', not_found),
]