from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.utils.html import format_html, strip_tags
from .models import NewsCategory , NewsPost


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'is_featured', 'publish_date', 'view_count')
    list_filter = ('is_published', 'is_featured', 'category', 'publish_date')
    search_fields = ('title', 'excerpt', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_date'

    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'category', 'excerpt', 'content')
        }),
        ('Images', {
            'fields': ('featured_image', 'featured_image_alt')
        }),
        ('SEO', {
            'fields': ('meta_description',)
        }),
        ('Publishing', {
            'fields': ('is_published', 'is_featured', 'publish_date')
        }),
        ('Statistics', {
            'fields': ('view_count',),
            'classes': ('collapse',)
        }),
    )

    def content_preview(self, obj):
        content = strip_tags(obj.content)
        return content[:100] + "..." if len(content) > 100 else content

    content_preview.short_description = 'Content Preview'

    actions = ['mark_published', 'mark_unpublished']

    def mark_published(self, request, queryset):
        from django.utils import timezone
        updated = queryset.update(is_published=True, publish_date=timezone.now())
        self.message_user(request, f'{updated} posts marked as published.')

    mark_published.short_description = "Publish selected posts"

    def mark_unpublished(self, request, queryset):
        updated = queryset.update(is_published=False)
        self.message_user(request, f'{updated} posts marked as unpublished.')

    mark_unpublished.short_description = "Unpublish selected posts"