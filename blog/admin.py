from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['slug', "publish", "update"]
admin.site.register(Post, PostAdmin)