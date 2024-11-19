from django.db import models

# Create your models here.

class Add_model(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    Answer = models.IntegerField()

class Sub_model(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    Answer = models.IntegerField()

class Multi_model(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    Answer = models.IntegerField()

class Div_model(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    Answer = models.IntegerField()

class CircleArea_model(models.Model):
    radius = models.FloatField()
    area = models.FloatField()

class TriangleArea_model(models.Model):
    base = models.FloatField()
    height = models.FloatField()
    area = models.FloatField()

class FilmCreateModel(models.Model):
    films_name = models.CharField(max_length=50)
    release_date = models.DateField()
    director = models.CharField(max_length=20)
