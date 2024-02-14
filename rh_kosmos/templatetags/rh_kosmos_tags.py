from PIL import Image
from django import template

register = template.Library()


@register.filter()
def mymedia(data):
    if data:
        img = Image.open(data.path)

        max_size = max(img.width, img.height)

        new_img = Image.new("RGB", (max_size, max_size), "white")
        new_img.paste(img, ((max_size - img.width) // 2, (max_size - img.height) // 2))

        new_img.save(data.path)

        return f'/media/{data}'
    return '#'
