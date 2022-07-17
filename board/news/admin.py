from django.contrib import admin
from .models import Post, ImagePost, FilePost




admin.site.register(Post)
admin.site.register(ImagePost)
admin.site.register(FilePost)

