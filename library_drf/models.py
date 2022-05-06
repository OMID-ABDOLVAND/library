from django.db import models

# Create your models here.
from django.db.models import Model


class Book(models.Model):
    name = models.CharField(max_length=225)
    author = models.CharField(max_length=225)
    Genre = models.CharField(max_length=225)
    published = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

