
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Prepare to store authors with their books
    author_books = []

    # Loop through the authors
    for author in authors:
        # Get active books for the current author
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')
        author_books.append({
            'author': author,
            'books': books
        })

    _vars['author_books'] = author_books

    return render(request, 'template.html', _vars)
