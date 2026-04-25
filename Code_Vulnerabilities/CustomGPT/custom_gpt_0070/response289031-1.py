
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()  # Prefetch related books

    # Create a dictionary to hold authors and their active books
    author_books = {}

    for author in authors:
        # Fetch active books for the current author
        books = Book.objects.filter(author=author, is_active=True)
        author_books[author] = books  # Store the books in a dict

    _vars['author_books'] = author_books  # Pass this dict to the template

    return render(request, 'template.html', _vars)
