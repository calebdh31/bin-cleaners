from django.contrib import admin
from .models import Booking

admin.site.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'service_type', 'date', 'status')
    list_filter = ('status',)
    search_fields = ('user__username', 'address', 'service_type', 'status')