from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html
from .models import SiteSettings, HomePage


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Information', {
            'fields': ('site_name', 'tagline')
        }),
        ('Contact Information', {
            'fields': ('phone', 'email', 'address')
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'instagram_url', 'youtube_url')
        }),
        ('About Page Content', {
            'fields': ('vision_text', 'who_we_are_text', 'why_choose_us_text')
        }),
        ('Home Page Features', {
            'fields': ('feature_immersive', 'feature_outdoor', 'feature_building')
        }),
    )

    def has_add_permission(self, request):
        # Only allow one SiteSettings instance
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Don't allow deletion of site settings
        return False

    class HomePageAdmin(admin.ModelAdmin):
        list_display = ('hero_title', 'is_active', 'years_operating', 'updated_at')
        list_filter = ('is_active', 'created_at')
        fieldsets = (
            ('Hero Section', {
                'fields': ('hero_image', 'hero_title', 'hero_subtitle')
            }),
            ('Statistics', {
                'fields': ('years_operating', 'children_served')
            }),
            ('Status', {
                'fields': ('is_active',)
            }),
        )

        def has_add_permission(self, request):
            # Only allow one HomePage instance
            return not HomePage.objects.exists()