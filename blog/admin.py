from django.contrib import admin
from .models import Article, Post

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', "publish", "update"]
admin.site.register(Post, PostAdmin)

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', "publish", "update"]
admin.site.register(Article, ArticleAdmin)