from django.db import models

# Create your models here.


# Book[id,title,author,price,langauge,genre,year]

class Book(models.Model):

    title=models.CharField(max_length=200)

    author=models.CharField(max_length=250)

    price=models.PositiveIntegerField()

    language=models.CharField(max_length=200)

    genre=models.CharField(max_length=100)

    year=models.CharField(max_length=10)

    image = models.ImageField(upload_to="bookimages", null=True)

    def __str__(self):
        return self.title

