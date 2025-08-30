


# Create your models here.
from django.db import models

class VolunteerApplication(models.Model):
    VOLUNTEER_TYPES = [
        ('plain', 'Plain Volunteering'),
        ('teaching', 'Teaching Volunteering'),
        ('technical', 'Technical Volunteering'),
        ('other', 'other'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    role = models.CharField(max_length=20, choices=(VOLUNTEER_TYPES))
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.role}"


