from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.core.validators import RegexValidator


class SiteSettings(models.Model):
    """Global site settings and content"""
    site_name = models.CharField(max_length=200, default="Forest School Cyprus")
    tagline = models.CharField(max_length=300, default="Where children grow, learn, and thrive in nature.")

    # Contact Information
    phone = models.CharField(max_length=20, default="+357 9980 3654")
    email = models.EmailField(default="forestschool.cy@gmail.com")
    address = models.TextField(default="Agiou Alexandrou Street, Kornos")

    # Social Media
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)

    # About Content
    vision_text = RichTextField()
    who_we_are_text = RichTextField()
    why_choose_us_text = RichTextField()

    # Home Page Features
    feature_immersive = models.CharField(max_length=200, default="An immersive, nature-based learning experience")
    feature_outdoor = models.CharField(max_length=200, default="100% outdoor, inquiry-driven, and child-led learning")
    feature_building = models.CharField(max_length=200,
                                        default="Building confidence, resilience, and environmental stewardship")

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.site_name


class HomePage(models.Model):
    """Home page specific content"""
    hero_image = models.ImageField(upload_to='home/', blank=True)
    hero_title = models.CharField(max_length=200, default="Welcome to Forest School Cyprus")
    hero_subtitle = models.TextField(default="Where children grow, learn, and thrive in nature.")

    # Statistics or highlights
    years_operating = models.IntegerField(default=7, help_text="Years in operation")
    children_served = models.IntegerField(default=200, help_text="Total children served")

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Home Page Content"
        verbose_name_plural = "Home Page Content"

    def __str__(self):
        return f"Home Page - {self.hero_title}"
