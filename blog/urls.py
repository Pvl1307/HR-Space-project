from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostDetailView, BlogListView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('blog_detail/<int:pk>/', PostDetailView.as_view(), name='blog_detail'),
]
