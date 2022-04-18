from django.contrib import admin

# Register your models here.
# import class Post
from .models import Post

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', "publish", "update"]

admin.site.register(Post, PostAdmin)