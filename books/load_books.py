from .models import Book
from googlebooks.googlebooks import fetch_books

def load_books():
    books = fetch_books(0, 15)
    for book in books:
        Book.objects.create(
            book_id=book['id'],
            title=book['title'],
            subtitle=book['subtitle'],
            authors=book['authors'],
            publisher=book['publisher'],
            published_date=book['published_date'],
            description=book['description'],
            categories=book['categories'],
            thumbnail=book['thumbnail']
        )
