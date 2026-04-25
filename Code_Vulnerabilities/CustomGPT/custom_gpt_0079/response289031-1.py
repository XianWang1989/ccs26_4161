
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Pre-fetch related books to minimize database queries
    for author in authors:
        # Fetch active books for each author
        books = Book.objects.filter(author=author, is_active=True)
        author.books = books  # Adding a custom attribute to the author

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
