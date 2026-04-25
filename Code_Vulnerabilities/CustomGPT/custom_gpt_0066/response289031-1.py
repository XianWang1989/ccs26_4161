
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Create a list to store authors with their books
    authors_with_books = []

    # Loop through the authors
    for author in authors:
        # Filter books for each author that are active
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')

        # Append author and their books to the list
        authors_with_books.append({
            'author': author,
            'books': books
        })

    _vars['authors'] = authors_with_books

    return render(request, 'template.html', _vars)
