
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Add a books attribute to each author
    for author in authors:
        # Fetch active books for this author
        author.books = Book.objects.filter(author=author, is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
