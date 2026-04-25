
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}

    # Get all authors
    authors = Author.objects.all()

    # Loop through authors and add their active books
    for author in authors:
        # Fetch active books for the author
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')
        author.books = books  # Attach the books to the author object

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
