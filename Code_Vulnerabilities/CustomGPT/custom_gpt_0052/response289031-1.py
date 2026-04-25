
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Prepare a list to hold authors with their active books
    author_books = []

    # Loop through the authors
    for author in authors:
        # Fetch active books for the author
        books = Book.objects.filter(author=author, is_active=True)
        author_books.append({
            'author': author,
            'books': books
        })

    _vars['author_books'] = author_books

    return render(request, 'template.html', _vars)
