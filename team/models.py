from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.core.validators import RegexValidator
# Create your models here.
class TeamMember(models.Model):
    """Staff and team member profiles"""
    ROLE_CHOICES = [
        ('pedagogue', 'Pedagogue'),
        ('coordinator', 'Program Coordinator'),
        ('volunteer', 'Volunteer'),
        ('director', 'Director'),
        ('assistant', 'Assistant'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    title_greek = models.CharField(max_length=200, blank=True, help_text="Title in Greek")

    # Profile Information
    photo = models.ImageField(upload_to='team/', blank=True)
    bio = RichTextField(help_text="Professional biography")
    qualifications = RichTextField(blank=True)
    specialties = models.CharField(max_length=300, blank=True, help_text="Areas of expertise")

    # Contact (optional for some staff)
    email = models.EmailField(blank=True)

    # Display Settings
    is_featured = models.BooleanField(default=False, help_text="Show on main team page")
    display_order = models.IntegerField(default=0, help_text="Order of appearance")
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', 'last_name']
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_role_display()}"

    def get_absolute_url(self):
        return reverse('team:profile', kwargs={'pk': self.pk})

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
