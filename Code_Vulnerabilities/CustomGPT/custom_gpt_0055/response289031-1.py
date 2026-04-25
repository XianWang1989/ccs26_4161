
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    # Use prefetch_related to get all authors and their active books in one query
    authors = Author.objects.prefetch_related(
        'book_set'  # Use the related name for foreign keys
    ).filter(is_active=True)

    # Iterate through authors and filter their books
    for author in authors:
        # Filter books that are active for each author
        author.active_books = author.book_set.filter(is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
