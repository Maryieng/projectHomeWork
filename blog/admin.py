from django.contrib import admin

from blog.models import Blogpost


@admin.register(Blogpost)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'preview', 'created_at', 'publication_sign')
    list_filter = ('publication_sign', 'view_count')
