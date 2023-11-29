from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author']
    list_display_links = ['id', 'title']
    search_fields = ['id', 'title']
    list_filter = ['author']


admin.site.register(Post, PostAdmin)
