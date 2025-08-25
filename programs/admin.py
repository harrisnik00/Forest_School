from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html
from .models import Camp


@admin.register(Camp)
class CampAdmin(admin.ModelAdmin):
    list_display = ('name', 'season', 'year', 'start_date', 'end_date', 'enrollment_status', 'is_open_for_registration')
    list_filter = ('season', 'year', 'is_open_for_registration', 'is_featured')
    search_fields = ('name', 'description')
    date_hierarchy = 'start_date'

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'season', 'year')
        }),
        ('Content', {
            'fields': ('description', 'activities', 'featured_image')
        }),
        ('Schedule', {
            'fields': ('start_date', 'end_date', 'daily_schedule')
        }),
        ('Enrollment', {
            'fields': ('age_group', 'max_participants', 'current_enrollment')
        }),
        ('Pricing', {
            'fields': ('daily_fee', 'weekly_fee')
        }),
        ('Settings', {
            'fields': ('is_open_for_registration', 'is_featured')
        }),
    )

    def enrollment_status(self, obj):
        percentage = (obj.current_enrollment / obj.max_participants) * 100
        color = 'red' if percentage >= 100 else 'orange' if percentage >= 80 else 'green'
        return format_html(
            '<span style="color: {};">{}/{} ({}%)</span>',
            color, obj.current_enrollment, obj.max_participants, int(percentage)
        )

    enrollment_status.short_description = 'Enrollment'