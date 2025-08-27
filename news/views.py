from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import NewsPost, NewsCategory


class NewsListView(ListView):
    model = NewsPost
    template_name = 'news/list.core'
    context_object_name = 'news_posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = NewsPost.objects.filter(is_published=True)
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(NewsCategory, slug=category_slug)
            queryset = queryset.filter(category=category)
        return queryset.order_by('-publish_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = NewsCategory.objects.all()
        context['featured_posts'] = NewsPost.objects.filter(
            is_published=True,
            is_featured=True
        )[:3]
        return context


class NewsDetailView(DetailView):
    model = NewsPost
    template_name = 'news/detail.core'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return NewsPost.objects.filter(is_published=True)

    def get_object(self):
        obj = super().get_object()
        # Increment view count
        obj.view_count += 1
        obj.save(update_fields=['view_count'])
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_posts'] = NewsPost.objects.filter(
            is_published=True,
            category=self.object.category
        ).exclude(pk=self.object.pk)[:3]
        return context