from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    category = models.CharField(max_length=50, default='blog')
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now= True)
    slug = models.SlugField(blank=True, editable=False)

    # auto generate slug
    def save(self):
        # create slug from title
        self.slug = slugify(self.title)
        # save slug
        super(Post, self).save()
    """ 
        title, body = field name,
        CharField,TextField = data type,
        max_length = option
    """

    def __str__(self) :
        return f"{self.id}. {self.title}"