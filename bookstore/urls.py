from django.urls import path

from .views import book_detail, show_books, show_author

urlpatterns = [
    path('books', show_books, name='book_list'),
    path('books/<int:index>', book_detail, name='book_detail'),
    path('author/<int:id>', show_author, name='author'),
]
