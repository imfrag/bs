from django.urls import path
from .views import signin, signup


urlpatterns = [
    # level(1:user, 2:manager, 3:admin)
    path('signin/<int:level>/', signin, name='signin'),
    path('signup/', signup, name='signup'),
]