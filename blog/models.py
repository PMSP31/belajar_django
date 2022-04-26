from django.db import models
from django.template.defaultfilters import slugify
from .validators import validate_title

# Create your models here.
class Post(models.Model):
    LIST_CATEGORY=(
        ('blog','Blog'),
        ('jurnal', 'Jurnal')
    )
    
    title = models.CharField(
            max_length=255, 
            validators=[validate_title]
        )
    body = models.TextField()
    category = models.CharField(
            max_length=50, 
            default='blog', 
            choices=LIST_CATEGORY
        )
    publish = models.DateTimeField(
            auto_now_add=True
        )
    update = models.DateTimeField(
            auto_now= True
        )
    slug = models.SlugField(
            blank=True, 
            editable=False
        )

    def save(self, *args, **kwargs):
        # create slug from title
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self) :
        return f"{self.id}. {self.title}"

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self) :
        return f"{self.id}. {self.title}"