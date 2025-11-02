from . import views
from django.urls import path

urlpatterns = [
    path('', views.user_bookings, name='user_bookings')
]