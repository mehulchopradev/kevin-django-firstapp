from django.db import models
from datetime import date

# Create your models here.

class Student(models.Model):
    # id
    username = models.CharField(unique=True, max_length=50, null=False, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=3, null=True)
    gender = models.CharField(max_length=1, null=False)

class PublicationHouse(models.Model):
    # id
    name = models.CharField(max_length=50, null=False, blank=False)
    ratings = models.IntegerField(null=False)

    # 1 pub house can publish many books (one to many)

class Book(models.Model):
    # id
    title = models.CharField(max_length=50, null=False, blank=False)
    price = models.FloatField(null=True)
    pages = models.IntegerField(null=False)
    no_of_copies = models.IntegerField(null=False)
    published_date = models.DateField(null=True, default=date.today())
    publication_house = models.ForeignKey(PublicationHouse, on_delete=models.CASCADE)

    # 1 book can only be published by a particular pub house (many to one)

    def __str__(self):
        return self.title