from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy

# Create your models here.

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

    def get_absolute_url(self):
        return reverse_lazy('article:detail', kwargs={'slug': self.slug})

    def __str__(self) :
        return f"{self.id}. {self.title}"