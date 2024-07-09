from django.contrib import admin
from .models import Book, BookRead, BookLike, BookDislike, BookRating

# Register your models here.
admin.site.register(Book)
admin.site.register(BookRead)
admin.site.register(BookLike)
admin.site.register(BookDislike)
admin.site.register(BookRating)
