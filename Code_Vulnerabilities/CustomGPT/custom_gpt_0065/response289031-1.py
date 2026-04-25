
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all().prefetch_related('book_set')  # Use prefetch_related for efficient querying

    # Create an empty list to hold author details and their books
    author_details = []

    # Loop through authors
    for author in authors:
        # Get active books for each author
        books = author.book_set.filter(is_active=True)  # Access related books directly

        # Append author information and their books to the list
        author_details.append({
            'author': author,
            'books': books
        })

    _vars['author_details'] = author_details

    return render(request, 'template.html', _vars)
