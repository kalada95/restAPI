from django.db import models
from AppOne.models import Book

class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField()
    birth_date = models.DateField()
    books_published = models.ManyToManyField(Book,related_name="authors")

    def __str__(self):
        return self.name


