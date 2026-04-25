
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Pre-fetch related books for all authors to avoid multiple queries
    for author in authors:
        author.books = Book.objects.filter(author=author, is_active=True)

    _vars['authors'] = authors
    return render(request, 'template.html', _vars)
