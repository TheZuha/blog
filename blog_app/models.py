from django.db import models
from django.utils.html import format_html
import re


# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def content_display(self):
        # URL manzillarni matn ichida ko'k rangda ko'rsatish
        content = self.content

        # URL-larni HTML <a> teglariga o'zgartirish
        content = re.sub(
            r'(https?://\S+)',
            r'<a href="\1" style="color: blue;">\1</a>',
            content
        )

        return format_html(content)
