
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Creating a dictionary to hold authors and their books
    authors_with_books = []

    # Loop through the authors
    for author in authors:
        # Get active books for this author
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')

        # Append the author's details and their active books
        authors_with_books.append({
            'author': author,
            'books': books
        })

    _vars['authors_with_books'] = authors_with_books

    return render(request, 'template.html', _vars)
