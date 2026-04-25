
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}

    # Using prefetch_related to fetch books associated with authors efficiently
    authors = Author.objects.prefetch_related('book_set').all()

    # Loop through the authors and attach their active books
    for author in authors:
        # Filter books for each author that are active
        author.active_books = author.book_set.filter(is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
