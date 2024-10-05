from django.contrib import admin
from django.utils.html import format_html
from django.db import models
from django_summernote.widgets import SummernoteWidget
from .models import Blogs


# Register your models here.

class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_display', 'created_at')
    fields = ('title', 'content', 'image')

    formfield_overrides = {
        models.TextField: {'widget': SummernoteWidget},
    }

    def content_display(self, obj):
        # URL manzillarni matn ichida ko'k rangda ko'rsatish
        content = obj.content
        content = content.replace('http://', '<a href="http://">http://</a>')
        content = content.replace('https://', '<a href="https://">https://</a>')
        return format_html(content)

    content_display.short_description = 'Content'


admin.site.register(Blogs, BlogsAdmin)
