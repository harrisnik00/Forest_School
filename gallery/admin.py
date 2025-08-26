from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from .models import GalleryCategory, Photo


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'photo_count')
    prepopulated_fields = {'slug': ('name',)}

    def photo_count(self, obj):
        return obj.photo_set.count()

    photo_count.short_description = 'Photos'


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image_preview', 'is_public', 'requires_consent', 'taken_date')
    list_filter = ('category', 'is_public', 'requires_consent', 'taken_date')
    search_fields = ('title', 'caption', 'alt_text')
    date_hierarchy = 'taken_date'

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'category', 'image', 'alt_text', 'caption')
        }),
        ('Privacy & Permissions', {
            'fields': ('requires_consent', 'is_public')
        }),
        ('Metadata', {
            'fields': ('taken_date', 'photographer')
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 60px; height: 60px; object-fit: cover;" />',
                obj.image.url
            )
        return "No Image"

    image_preview.short_description = "Preview"