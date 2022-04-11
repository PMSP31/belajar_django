from django.contrib import admin

# Register your models here.
# import class Post
from .models import Post

admin.site.register(Post)