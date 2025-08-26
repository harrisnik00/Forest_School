from django.contrib import admin
from django.db import models
# Register your models here.
class VolunteerApplication(models.Model):
    VOLUNTEER_CHOICES = [
        ("plain", "Plain Volunteering"),
        ("teaching", "Teaching Volunteering"),
        ("technical", "Technical Volunteering"),
        ("other", "Άλλο"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, choices=VOLUNTEER_CHOICES)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_type_display()}"