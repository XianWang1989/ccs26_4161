
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all()

    for author in authors:
        # Fetching active books for the author
        books = Book.objects.filter(author=author, is_active=True)
        author.books = books  # Assign the list of books to a new attribute on the author instance

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
