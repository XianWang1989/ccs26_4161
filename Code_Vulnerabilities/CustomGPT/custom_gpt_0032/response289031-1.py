
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Loop through authors and attach active books
    for author in authors:
        # Get the active books for each author
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')
        # Attach books to the author object
        author.books = books

    _vars['authors'] = authors
    return render(request, 'template.html', _vars)
