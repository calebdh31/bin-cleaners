from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from . import views
from django.contrib.auth import views as auth_views


def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('bookings/', include('bookings.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]
