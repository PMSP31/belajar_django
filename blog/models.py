from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=30, default='yourname')
    title = models.CharField(max_length=255)
    body = models.TextField()
    email = models.EmailField(default='your@email.com')
    time_post = models.DateTimeField(auto_now_add = True)

    """ 
        title, body = field name,
        CharField,TextField = data type,
        max_length = option
    """

    def __str__(self) :
        return f"{self.id}. {self.title}"