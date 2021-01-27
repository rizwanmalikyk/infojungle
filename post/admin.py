from django.contrib import admin

from .models import Author, category, Post, Comment, PostView

admin.site.register(Author)
admin.site.register(category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)
