from django.db import models

# Create your models here.
class Sosmed(models.Model) :
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    username = models.CharField(max_length=30)
    content = models.CharField(max_length=30)

    def __str__(self) :
        return f"{self.id}. {self.username}"