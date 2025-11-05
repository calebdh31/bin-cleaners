from . import views
from django.urls import path

urlpatterns = [
    path('', views.user_bookings, name='user_bookings'),
    path('new/', views.BookingCreate.as_view(), name='new_booking'),
    path('<int:pk>/update/', views.BookingUpdate.as_view(), name='update_booking'),
    path('<int:pk>/delete/', views.BookingDelete.as_view(), name='delete_booking'),
    path('admin/', views.admin_bookings, name='admin_bookings')
]