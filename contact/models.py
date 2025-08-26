from django.db import models
from ckeditor.fields import RichTextField
class ContactMessage(models.Model):
    """
    Stores messages sent from the contact form.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
# Create your models here.
class Program(models.Model):
    """Educational programs offered"""
    PROGRAM_TYPES = [
        ('morning', 'Morning School'),
        ('afternoon', 'Afternoon Program'),
        ('weekend', 'Weekend Program'),
        ('camp', 'Holiday Camp'),
    ]

    AGE_GROUPS = [
        ('2-3', '2-3 years'),
        ('3-6', '3-6 years'),
        ('4-10', '4-10 years'),
        ('mixed', 'Mixed ages'),
    ]

    name = models.CharField(max_length=200)
    program_type = models.CharField(max_length=20, choices=PROGRAM_TYPES)
    age_group = models.CharField(max_length=10, choices=AGE_GROUPS)

    description = RichTextField()
    schedule = models.CharField(max_length=200, help_text="e.g., 8:00 AM - 2:30 PM")

    # Pricing
    is_flexible_pricing = models.BooleanField(default=True)
    includes_meals = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['program_type', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_age_group_display()})"


class PricingOption(models.Model):
    """Pricing packages for programs"""
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='pricing_options')

    name = models.CharField(max_length=100, help_text="e.g., 5 days/week")
    days_per_week = models.IntegerField()
    monthly_fee = models.DecimalField(max_digits=6, decimal_places=2)
    daily_fee = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    is_popular = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-days_per_week']

    def __str__(self):
        return f"{self.program.name} - {self.name} (€{self.monthly_fee}/month)"


class Inquiry(models.Model):
    """General inquiries and contact form submissions"""
    INQUIRY_TYPES = [
        ('admission', 'Admission Inquiry'),
        ('general', 'General Information'),
        ('volunteer', 'Volunteering'),
        ('partnership', 'Partnership'),
        ('media', 'Media Inquiry'),
    ]

    # Contact Information
    parent_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    # Child Information (if applicable)
    child_name = models.CharField(max_length=200, blank=True)
    child_age = models.IntegerField(blank=True, null=True)

    # Inquiry Details
    inquiry_type = models.CharField(max_length=20, choices=INQUIRY_TYPES)
    program_interest = models.ForeignKey(Program, on_delete=models.SET_NULL, blank=True, null=True)
    message = models.TextField()

    # Admin Fields
    is_responded = models.BooleanField(default=False)
    response_notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    responded_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Inquiries"

    def __str__(self):
        return f"{self.parent_name} - {self.get_inquiry_type_display()}"
