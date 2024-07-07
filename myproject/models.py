from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)

class Read_Books(models.Model):
    title = models.CharField(max_length=100)

class Rate_Books(models.Model):
    title = models.CharField(max_length=100)

class Like_Books(models.Model):
    title = models.CharField(max_length=100)

class Algorithm(models.Model):
    liked_books = models.CharField(max_length=100)
    disliked_books = models.CharField(max_length=100)
