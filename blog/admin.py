from django.contrib import admin

from blog.models import Category, Post, Comment, Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'content', 'published_at',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('to_post', 'author', 'content', 'published_at',)


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('owner', 'content', 'mark',)
