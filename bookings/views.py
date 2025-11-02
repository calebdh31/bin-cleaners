from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Booking


def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/index.html', {'bookings': bookings})

