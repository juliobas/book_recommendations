from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Book, BookRead, BookLike, BookRating, BookDislike
from .serializers import BookSerializer, UserSerializer, BookReadSerializer, BookLikeSerializer, BookDislikeSerializer, BookRatingSerializer
from utils.ResponseUtil import ResponseUtil
from .load_books import load_books
from .recommend_books import recommend_books

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        books = self.get_queryset()
        if books.count() == 0:
            load_books()

        recommended_books = recommend_books(request.user)
        serializer = self.get_serializer(recommended_books, many=True)
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

class BookReadCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = BookReadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(ResponseUtil.success("Book Read Created", serializer.data))
        return Response(ResponseUtil.error("Error", serializer.errors))

class UserBookReadList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=request.user.id)
        books_read_ids = BookRead.objects.filter(user=user).values_list('book_id', flat=True)
        books = Book.objects.filter(id__in=books_read_ids)
                
        serializer = BookSerializer(books, many=True)
        return Response(ResponseUtil.success("Books Read Lists", serializer.data))

class BookLikeCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = BookLikeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(ResponseUtil.success("Book Like Created", serializer.data))
        return Response(ResponseUtil.error("Error", serializer.errors))

class BookLikeList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=request.user.id)
        books_like_ids = BookLike.objects.filter(user=user).values_list('book_id', flat=True)
        books = Book.objects.filter(id__in=books_like_ids)

        serializer = BookSerializer(books, many=True)
        return Response(ResponseUtil.success("Books Like Lists", serializer.data))

class BookDislikeCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = BookDislikeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(ResponseUtil.success("Book Dislike Created", serializer.data))
        return Response(ResponseUtil.error("Error", serializer.errors))
    
class BookDislikeList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=request.user.id)
        books_dislike_ids = BookDislike.objects.filter(user=user).values_list('book_id', flat=True)
        books = Book.objects.filter(id__in=books_dislike_ids)

        serializer = BookSerializer(books, many=True)
        return Response(ResponseUtil.success("Books Dislike Lists", serializer.data))
    
class BookRatingCreate(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = BookRatingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(ResponseUtil.success("Book Rating Created", serializer.data))
        return Response(ResponseUtil.error("Error", serializer.errors))
class BookRatingList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=request.user.id)
        books_rating_ids = BookRating.objects.filter(user=user).values_list('book_id', flat=True)
        books = Book.objects.filter(id__in=books_rating_ids)

        serializer = BookSerializer(books, many=True)
        return Response(ResponseUtil.success("Books Rating Lists", serializer.data))