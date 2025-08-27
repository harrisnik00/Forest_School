from django.urls import path
from . import views

app_name = 'camps'

urlpatterns = [
    path('', views.CampListView.as_view(), name='list'),
    path('<int:pk>/', views.CampDetailView.as_view(), name='detail'),
]