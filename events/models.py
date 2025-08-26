from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Event(models.Model):
    """Calendar events, open days, workshops"""
    EVENT_TYPES = [
        ('open_day', 'Open Day'),
        ('workshop', 'Workshop'),
        ('parent_meeting', 'Parent Meeting'),
        ('community', 'Community Event'),
        ('training', 'Training'),
    ]

    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)

    description = RichTextField()

    # Date and Time
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    is_all_day = models.BooleanField(default=False)

    # Location
    location = models.CharField(max_length=300, default="Forest School Cyprus, Kornos")
    location_details = models.TextField(blank=True)

    # Registration
    requires_registration = models.BooleanField(default=False)
    max_participants = models.IntegerField(blank=True, null=True)
    registration_deadline = models.DateTimeField(blank=True, null=True)

    # Images
    featured_image = models.ImageField(upload_to='events/', blank=True)

    # Status
    is_published = models.BooleanField(default=True)
    is_cancelled = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['start_datetime']

    def __str__(self):
        return f"{self.title} - {self.start_datetime.strftime('%Y-%m-%d')}"
