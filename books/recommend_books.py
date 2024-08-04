from .models import Book, BookRead, BookLike, BookRating, BookDislike
from django.db.models import Count, Avg, Q, Value, FloatField
from django.db.models.functions import Coalesce
from .load_books import load_books
import json
from django.db.models.expressions import RawSQL
from django.db.models import Q

def get_user_preferences(user):
    liked_books = BookLike.objects.filter(user_id=user.id).values_list('book', flat=True)
    read_books = BookRead.objects.filter(user_id=user.id).values_list('book', flat=True)
    disliked_books = BookDislike.objects.filter(user_id=user.id).values_list('book', flat=True)

    potential_books = Book.objects.filter(
        Q(id__in=liked_books) | Q(id__in=read_books)
    ).exclude(id__in=disliked_books)

    authors = potential_books.values_list('authors', flat=True)
    categories = potential_books.values_list('categories', flat=True)

    author_list = []
    for author in authors:
        author_list.extend(author)
    author_list = list(set(author_list))

    category_list = []
    for category in categories:
        category_list.extend(category)
    category_list = list(set(category_list))

    return author_list, category_list, read_books, liked_books

def recommend_books(user):
    num_executions = 0
    while True:
        authors, categories, read_books, liked_books = get_user_preferences(user)

        if not authors and not categories and not read_books and not liked_books:
            recommended_books = Book.objects.all().annotate(average_rating=Coalesce(Avg('bookrating__rating'), Value(0), output_field=FloatField())).order_by('-average_rating')[:15]
        else:
            print("Entre al algoritmo")
            conditions = []
            for category in categories:
                condition = f"JSON_CONTAINS(categories, '{json.dumps(category)}', '$')"
                conditions.append(condition)
            
            category_final_condition = ' OR '.join(conditions)

            conditions = []
            for author in authors:
                condition = f"JSON_CONTAINS(authors, '{json.dumps(author)}', '$')"
                conditions.append(condition)
            
            author_final_condition = ' OR '.join(conditions)
          
            recommended_books = Book.objects.exclude(id__in=read_books).exclude(id__in=liked_books).annotate(
                author_match=RawSQL(author_final_condition, ()),
                categories_match=RawSQL(category_final_condition, ()),
                average_rating=Coalesce(Avg('bookrating__rating'), Value(0), output_field=FloatField())
            ).filter(Q(author_match=True) | Q(categories_match=True)).order_by('-average_rating')[:15]

        if recommended_books.count() > 0 or num_executions > 2:
            break
        else:
            if Book.objects.count() < 45:
                load_books(Book.objects.count(), Book.objects.count() + 15)
            else:
                print("Books limit reached.")
                break
            print("No books found. Loading more books.")
        
        num_executions += 1

    return recommended_books
    
