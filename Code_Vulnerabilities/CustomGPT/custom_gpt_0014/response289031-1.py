
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()  # Use prefetch_related to fetch related books efficiently

    # Create a structure to hold authors and their active books
    author_books = []

    for author in authors:
        active_books = author.book_set.filter(is_active=True)  # Use related name for books
        author_books.append({
            'author': author,
            'books': active_books
        })

    _vars['author_books'] = author_books

    return render(request, 'template.html', _vars)
