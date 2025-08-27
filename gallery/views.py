from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Photo, GalleryCategory


class GalleryView(ListView):
    model = Photo
    template_name = 'gallery/gallery.html'
    context_object_name = 'photos'
    paginate_by = 24

    def get_queryset(self):
        queryset = Photo.objects.filter(is_public=True)
        category_slug = self.request.GET.get('category')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset.order_by('-taken_date', '-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = GalleryCategory.objects.all()
        context['selected_category'] = self.request.GET.get('category')
        return context