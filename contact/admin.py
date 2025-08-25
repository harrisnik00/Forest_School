from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Program, PricingOption, Inquiry


class PricingOptionInline(admin.TabularInline):
    model = PricingOption
    extra = 1
    fields = ('name', 'days_per_week', 'monthly_fee', 'daily_fee', 'is_popular', 'is_active')


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'program_type', 'age_group', 'is_active')
    list_filter = ('program_type', 'age_group', 'is_active')
    search_fields = ('name', 'description')
    inlines = [PricingOptionInline]

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'program_type', 'age_group')
        }),
        ('Details', {
            'fields': ('description', 'schedule')
        }),
        ('Options', {
            'fields': ('is_flexible_pricing', 'includes_meals', 'is_active')
        }),
    )


class InquiryAdmin(admin.ModelAdmin):
    list_display = ('parent_name', 'inquiry_type', 'child_name', 'is_responded', 'created_at')
    list_filter = ('inquiry_type', 'is_responded', 'created_at', 'program_interest')
    search_fields = ('parent_name', 'email', 'child_name', 'message')
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Contact Information', {
            'fields': ('parent_name', 'email', 'phone')
        }),
        ('Child Information', {
            'fields': ('child_name', 'child_age')
        }),
        ('Inquiry Details', {
            'fields': ('inquiry_type', 'program_interest', 'message')
        }),
        ('Admin Response', {
            'fields': ('is_responded', 'response_notes', 'responded_at')
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )

    actions = ['mark_as_responded']

    def mark_as_responded(self, request, queryset):
        from django.utils import timezone
        updated = queryset.update(is_responded=True, responded_at=timezone.now())
        self.message_user(request, f'{updated} inquiries marked as responded.')

    mark_as_responded.short_description = "Mark selected inquiries as responded"