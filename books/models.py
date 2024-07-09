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

class BookRead(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)    

    def __str__(self):
        return self.book.title

class BookLike(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)    

    def __str__(self):
        return self.book.title

class BookDislike(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)    

    def __str__(self):
        return self.book.title

class BookRating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)    
    rating = models.IntegerField()

    def __str__(self):
        return self.book.title + " - " + str(self.rating)