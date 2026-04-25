
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Loop through the authors and annotate with their active books
    for author in authors:
        # Retrieve active books for each author, using a list comprehension
        books = Book.objects.filter(author=author, is_active=True)
        # Add a new attribute to the author instance
        author.books = books

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
