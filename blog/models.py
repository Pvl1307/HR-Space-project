from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from users.models import User


class Category(models.Model):
    """Модель категорий статей"""
    name = models.CharField(max_length=100, verbose_name='Category of posts')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):
    """Модель поста в блоге"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category of post')
    title = models.CharField(max_length=200, verbose_name='Title of post')
    content = models.TextField(verbose_name='Content of post')
    published_at = models.DateTimeField(auto_now_add=True, verbose_name='Post published at')
    photo = models.ImageField(upload_to='blog/', verbose_name='Post photo')

    def __str__(self):
        return f'"{self.title}", published at {self.published_at}'

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Comment(models.Model):
    """Модель комменариев к посту """
    to_post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Comment to post')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author of comment')
    content = models.TextField(verbose_name='Content of comment')
    published_at = models.DateTimeField(auto_now_add=True, verbose_name='Comment pubkished at')

    def __str__(self):
        return f'{self.author}, published at {self.published_at}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class Reviews(models.Model):
    """Модель отзывов о сервисе"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Owner of review')
    content = models.TextField(verbose_name='Content of review')
    mark = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='Mark')

    def __str__(self):
        return f'{self.owner}, mark - {self.mark}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
