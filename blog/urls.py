# blog/urls.py

from django.urls import path
from .views import BlogCategoryListCreateView, PostListCreateView, PostDetailView

urlpatterns = [
    path('categories/', BlogCategoryListCreateView.as_view(), name='blog-category-list'),
    path('', PostListCreateView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]