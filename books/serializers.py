from rest_framework import serializers
from .models import Book, BookRead, BookLike
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
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