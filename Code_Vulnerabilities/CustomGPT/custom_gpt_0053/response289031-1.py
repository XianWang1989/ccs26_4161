
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}

    # Fetch all authors with their active books using prefetch_related
    authors = Author.objects.prefetch_related(
        'book_set'
    ).filter(is_active=True)

    # Create a list to hold authors and their active books
    authors_with_books = []

    for author in authors:
        # Filter active books for the current author
        active_books = author.book_set.filter(is_active=True)

        # Append author's data along with their active books
        authors_with_books.append({
            'author': author,
            'active_books': active_books
        })

    _vars['authors_with_books'] = authors_with_books

    return render(request, 'template.html', _vars)
