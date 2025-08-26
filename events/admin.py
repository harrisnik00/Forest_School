from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'start_datetime', 'status_display', 'requires_registration')
    list_filter = ('event_type', 'is_published', 'is_cancelled', 'requires_registration')
    search_fields = ('title', 'description', 'location')
    date_hierarchy = 'start_datetime'

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'event_type', 'description')
        }),
        ('Date & Time', {
            'fields': ('start_datetime', 'end_datetime', 'is_all_day')
        }),
        ('Location', {
            'fields': ('location', 'location_details')
        }),
        ('Registration', {
            'fields': ('requires_registration', 'max_participants', 'registration_deadline')
        }),
        ('Media', {
            'fields': ('featured_image',)
        }),
        ('Status', {
            'fields': ('is_published', 'is_cancelled')
        }),
    )

    def status_display(self, obj):
        if obj.is_cancelled:
            return format_html('<span style="color: red;">Cancelled</span>')
        elif not obj.is_published:
            return format_html('<span style="color: orange;">Draft</span>')
        else:
            return format_html('<span style="color: green;">Published</span>')

    status_display.short_description = 'Status'