
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all()

    for author in authors:
        # Fetching the books associated with the current author
        books = Book.objects.filter(author=author, is_active=True)
        author.books = books  # Set a new attribute to hold the books

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
