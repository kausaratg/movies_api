from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=10)
    image = models.CharField(max_length=300)
    categories = models.CharField(max_length=200, null=True)
    link = models.URLField(max_length=300)

    def __str__(self):
        return self.title