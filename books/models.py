from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=25)
    isbn_no = models.CharField(max_length=10,unique=True)
    author = models.CharField(max_length=30)
    published = models.DateField()

    def __str__(self):
        return self.name

