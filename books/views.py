from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Book
from .serializers import BookSerializer, UserSerializer
from utils.ResponseUtil import ResponseUtil
from .load_books import load_books

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        books = self.get_queryset()
        if books.count() == 0:
            load_books()
            books = Book.objects.all()
        serializer = self.get_serializer(books, many=True)
        return Response(ResponseUtil.success("Books Lists", serializer.data))

class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
