
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.
class NewsCategory(models.Model):
    """Categories for news articles"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "News Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class NewsPost(models.Model):
    """News articles and updates"""
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(NewsCategory, on_delete=models.SET_NULL, null=True, blank=True)

    excerpt = models.CharField(max_length=500, help_text="Brief summary for listings")
    content = RichTextField()

    # Images
    featured_image = models.ImageField(upload_to='news/', blank=True)
    featured_image_alt = models.CharField(max_length=200, blank=True)

    # SEO and Meta
    meta_description = models.CharField(max_length=160, blank=True)

    # Publishing
    is_published = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    publish_date = models.DateTimeField(blank=True, null=True)

    # Tracking
    view_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date', '-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news:detail', kwargs={'slug': self.slug})
