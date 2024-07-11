from django.urls import path
from .views import BookListView, UserProfileView, UserUpdateView, BookReadCreate, UserBookReadList

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('my_profile/', UserProfileView.as_view(), name='user_profile'),
    path('update_profile/', UserUpdateView.as_view(), name='user_update'),
    path('book_read/', BookReadCreate.as_view(), name='bookread-create'),
    path('my_books_read/', UserBookReadList.as_view(), name='user_books_read'),
]