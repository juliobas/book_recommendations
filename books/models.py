from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    authors = models.JSONField(default=list)
    publisher = models.CharField(max_length=200)
    published_date = models.CharField(max_length=20)
    description = models.TextField()
    categories = models.JSONField(default=list)
    thumbnail = models.CharField(max_length=1024)

    def __str__(self):
        return self.title
