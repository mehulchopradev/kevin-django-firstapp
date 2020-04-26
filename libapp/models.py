from django.db import models
from datetime import date

# Create your models here.

class Student(models.Model):
    # id
    username = models.CharField(unique=True, max_length=50, null=False, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=3, null=True)
    gender = models.CharField(max_length=1, null=False)

    # a student can issue more than 1 book (one to many) -- many to many

class PublicationHouse(models.Model):
    # id
    name = models.CharField(max_length=50, null=False, blank=False)
    ratings = models.IntegerField(null=False)

    # 1 pub house can publish many books (one to many)
    # book_set

    def __str__(self):
        return self.name

class Book(models.Model):
    # id
    title = models.CharField(max_length=50, null=False, blank=False)
    price = models.FloatField(null=True)
    pages = models.IntegerField(null=False)
    no_of_copies = models.IntegerField(null=False)
    published_date = models.DateField(null=True, default=date.today())
    publication_house = models.ForeignKey(PublicationHouse, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    # a book can be issued to more than one student (one to many) -- many to many

    # 1 book can only be published by a particular pub house (many to one)

    # 1 book can have many initial reviews (one to many)
    # review_set # implicit property in the one side of a one to many relationship

    def __str__(self):
        return self.title

class Review(models.Model):
    # id
    description = models.CharField(max_length=100, null=False, blank=False)
    full_name = models.CharField(max_length=20, null=False, blank=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    # A review can be associated with a specific book (many to one)