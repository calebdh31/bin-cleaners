from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    service_type = models.CharField(max_length=100)
    date = models.DateField()
    notes = models.TextField(blank=True)
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')
    
    def __str__(self):
        return f"{self.user.username} - {self.date} ({self.service_type})"


