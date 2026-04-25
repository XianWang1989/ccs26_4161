
from django.shortcuts import render
from .models import Author, Book  # Make sure to import your models

def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Create a custom list to hold authors and their active books
    authors_with_books = []

    # Loop through the authors
    for author in authors:
        # Get active books for each author
        books = Book.objects.filter(author=author, is_active=True)

        # Create a dictionary to hold the author and their books
        author_info = {
            'author': author,
            'books': books
        }
        authors_with_books.append(author_info)

    _vars['authors_with_books'] = authors_with_books

    return render(request, 'template.html', _vars)
