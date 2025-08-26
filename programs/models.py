
from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import RegexValidator
class Camp(models.Model):
    """Holiday camps and special programs"""
    
    CAMP_SEASONS = [
        ('easter', 'Easter Camp'),
        ('summer', 'Summer Camp'),
        ('christmas', 'Christmas Camp'),
        ('special', 'Special Event'),
    ]

    name = models.CharField(max_length=200)
    season = models.CharField(max_length=20, choices=CAMP_SEASONS)
    year = models.IntegerField()

    description = RichTextField()
    activities = RichTextField(help_text="List of activities and features")

    # Dates and Timing
    start_date = models.DateField()
    end_date = models.DateField()
    daily_schedule = models.CharField(max_length=200, blank=True)

    # Enrollment
    age_group = models.CharField(max_length=100, default="4-10 years")
    max_participants = models.IntegerField(default=20)
    current_enrollment = models.IntegerField(default=0)

    # Pricing
    daily_fee = models.DecimalField(max_digits=5, decimal_places=2)
    weekly_fee = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    # Images
    featured_image = models.ImageField(upload_to='camps/', blank=True)

    # Status
    is_open_for_registration = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-year', '-start_date']
        unique_together = ['season', 'year']

    def __str__(self):
        return f"{self.get_season_display()} {self.year}"

    @property
    def is_full(self):
        return self.current_enrollment >= self.max_participants

    @property
    def spots_remaining(self):
        return max(0, self.max_participants - self.current_enrollment)
