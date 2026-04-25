
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all().prefetch_related('book_set')  # Prefetch related books

    author_books = []  # Initialize a structure to store authors and their books

    # Loop through the authors
    for author in authors:
        books = Book.objects.filter(author=author, is_active=True)

        # Append to a custom dictionary or object
        author_books.append({
            'author': author,
            'books': books
        })

    _vars['author_books'] = author_books  # Pass the list of authors with their books

    return render(request, 'template.html', _vars)
