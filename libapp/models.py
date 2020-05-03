from django.db import models
from datetime import date

# Create your models here.

def upload_profile_pic(student, filename):
    # return a string from this function that should be the path on the server hard drive
    # where the uploaded image will be saved
    return 'images/profile/{0}/{1}_{2}'.format(student.username, student.username, filename)

class Student(models.Model):
    # id
    username = models.CharField(unique=True, max_length=50, null=False, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=3, null=True)
    gender = models.CharField(max_length=1, null=False)
    profilepicpath = models.ImageField(null=True, max_length=100, blank=True, upload_to=upload_profile_pic)

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
    students = models.ManyToManyField(Student, through='BooksIssued')

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

class BooksIssued(models.Model):
    # id
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    issue_date = models.DateField(null=False)
    return_date = models.DateField(null=True)