from django.db import models

# Create your models here.
class PageContent(models.Model):
    page = models.CharField(max_length=50, unique=True)  # "home", "about", "contact"
    text = models.TextField()
    image = models.ImageField(upload_to="page_images/", blank=True, null=True)

    def __str__(self):
        return self.page.capitalize()