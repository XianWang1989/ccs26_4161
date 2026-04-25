
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Annotate each author with their active books
    for author in authors:
        # Fetch books related to each author that are active
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')
        author.books = books  # Attach books to the author object

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
