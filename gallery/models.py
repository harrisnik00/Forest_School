from django.db import models


class GalleryCategory(models.Model):
    """Categories for organizing photos"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Gallery Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Photo(models.Model):
    """Individual photos in the gallery"""
    title = models.CharField(max_length=200)
    category = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL, null=True, blank=True)

    image = models.ImageField(upload_to='gallery/')
    alt_text = models.CharField(max_length=200, help_text="Accessibility description")
    caption = models.TextField(blank=True)

    # Privacy and permissions
    requires_consent = models.BooleanField(default=True, help_text="Photo includes children")
    is_public = models.BooleanField(default=True)

    # Metadata
    taken_date = models.DateField(blank=True, null=True)
    photographer = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-taken_date', '-created_at']

    def __str__(self):
        return self.title