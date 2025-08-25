from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role', 'is_featured', 'is_active', 'display_order')
    list_filter = ('role', 'is_featured', 'is_active')
    list_editable = ('display_order', 'is_featured', 'is_active')
    search_fields = ('first_name', 'last_name', 'bio')

    fieldsets = (
        ('Basic Information', {
            'fields': ('first_name', 'last_name', 'role', 'title_greek')
        }),
        ('Profile', {
            'fields': ('photo', 'bio', 'qualifications', 'specialties')
        }),
        ('Contact', {
            'fields': ('email',)
        }),
        ('Display Settings', {
            'fields': ('is_featured', 'display_order', 'is_active')
        }),
    )

    def photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 50%;" />',
                obj.photo.url)
        return "No Photo"

    photo_preview.short_description = "Photo"