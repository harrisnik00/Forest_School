from django.db import models

# Create your models here.
class GalleryImage(models.Model):
    """
    Photo gallery.
    """
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="gallery/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Image {self.id}"