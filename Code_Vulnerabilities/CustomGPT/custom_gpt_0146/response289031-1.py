
from django.shortcuts import render
from .models import Author, Book  # Make sure to import your models

def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Create a list to hold the author data with associated books
    author_data = []

    # Loop through the authors
    for author in authors:
        # Get all active books by this author
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')

        # Append the author's details along with their active books
        author_data.append({
            'author': author,
            'books': books
        })

    _vars['authors'] = author_data

    return render(request, 'template.html', _vars)
