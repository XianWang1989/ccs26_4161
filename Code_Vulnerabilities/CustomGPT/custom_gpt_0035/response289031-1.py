
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}

    # Fetch all authors with their active books in one query using select_related and prefetch_related
    authors = Author.objects.prefetch_related(
        'book_set'
    ).filter(is_active=True)

    _vars['authors'] = []

    # Loop through authors and filter books
    for author in authors:
        active_books = author.book_set.filter(is_active=True)
        _vars['authors'].append({
            'author': author,
            'books': active_books,
        })

    return render(request, 'template.html', _vars)
