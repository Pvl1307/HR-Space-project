import random

from celery import shared_task
from celery.utils.log import get_task_logger

from .models import Post, Category

logger = get_task_logger(__name__)


@shared_task
def change_post_category():
    categories = Category.objects.all()
    current_category = random.choice(categories)

    posts = Post.objects.filter(category=current_category).values()

    return list(posts)
