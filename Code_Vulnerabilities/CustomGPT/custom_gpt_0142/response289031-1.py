
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all().prefetch_related('book_set')  # Use prefetch_related to minimize database hits

    author_data = []

    # Loop through the authors
    for author in authors:
        # Get the books for the author that are active
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')

        # Append author data along with their active books list
        author_data.append({
            'author': author,
            'books': books
        })

    _vars['authors'] = author_data

    return render(request, 'template.html', _vars)
