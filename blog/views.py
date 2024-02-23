from django.shortcuts import render
from django.views.generic import DetailView, View

from blog.models import Post, Reviews
from blog.tasks import change_post_category
from rh_kosmos.models import RH


class BlogListView(View):
    template_name = 'blog/blog_list.html'

    def get(self, request, *args, **kwargs):
        change_post_category.delay()

        posts = Post.objects.filter(category=change_post_category)
        top_rh_list = RH.objects.filter(subscription=True)
        review = Reviews.objects.filter(mark__gte=4)

        context = {
            'post_list': posts,
            'rh_list': top_rh_list,
            'reviews_list': review
        }

        return render(request, self.template_name, context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
