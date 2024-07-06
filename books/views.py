from rest_framework import generics
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from utils.ResponseUtil import ResponseUtil
from .load_books import load_books

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        books = self.get_queryset()
        if books.count() == 0:
            load_books()
            books = Book.objects.all()
        serializer = self.get_serializer(books, many=True)
        return Response(ResponseUtil.success("Books Lists", serializer.data))
