from rest_framework import serializers
from .models import Book, BookRead, BookLike, BookDislike, BookRating
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(read_only=True)
    
    class Meta:
        model = Book
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        extra_kwargs = {'username': {'required': False}}

class BookReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRead
        fields = ['book', 'user']

class BookLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookLike
        fields = ['book', 'user']

class BookDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDislike
        fields = ['book', 'user']

class BookRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRating
        fields = ['book', 'user', 'rating']
