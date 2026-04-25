
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Create a list to hold authors and their books
    author_books = []

    # Loop through the authors
    for author in authors:
        # Get active books for the author
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')

        # Add the author and books to the list
        author_books.append({
            'author': author,
            'books': books
        })

    _vars['author_books'] = author_books

    return render(request, 'template.html', _vars)
