
from django.shortcuts import render
from .models import Author, Book  # Update with your actual models

def authors(request):
    _vars = {}
    authors = Author.objects.all()  # Get all authors
    authors_with_books = []

    # Loop through the authors
    for author in authors:
        # Fetch active books for the current author
        books = Book.objects.filter(author=author, is_active=True)
        authors_with_books.append({
            'author': author,
            'books': books
        })

    _vars['authors_with_books'] = authors_with_books

    return render(request, 'template.html', _vars)
