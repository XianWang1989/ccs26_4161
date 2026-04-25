
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Pre-fetch related books to avoid multiple queries
    for author in authors:
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')
        author.books = books  # Attach the books to the author object

    _vars['authors'] = authors
    return render(request, 'template.html', _vars)
