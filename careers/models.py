
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.db import models

class VolunteerApplication(models.Model):
    VOLUNTEER_TYPES = [
        ('plain', 'Plain Volunteering'),
        ('teaching', 'Teaching Volunteering'),
        ('technical', 'Technical Volunteering'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)

    volunteer_type = models.CharField(
        max_length=20,
        choices=VOLUNTEER_TYPES,
        help_text="Select the type of volunteering you are interested in."
    )

    message = models.TextField(blank=True)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_volunteer_type_display()}"