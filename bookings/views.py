from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Booking
from .forms import BookingForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def user_bookings(request):
    if request.user.is_superuser:
        bookings = Booking.objects.all()
        return render(request, 'bookings/index.html', {'bookings': bookings})
    else:
        bookings = Booking.objects.filter(user=request.user)
        return render(request, 'bookings/index.html', {'bookings': bookings})
    
@login_required
def admin_bookings(request):
    bookings = Booking.objects.filter()
    return render(request, 'bookings/index.html', {'bookings': bookings})

class BookingCreate(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('user_bookings')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class BookingUpdate(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('user_bookings')

class BookingDelete(LoginRequiredMixin, DeleteView):
    model = Booking
    success_url = reverse_lazy('user_bookings')
    template_name = 'bookings/booking_confirm_delete.html'