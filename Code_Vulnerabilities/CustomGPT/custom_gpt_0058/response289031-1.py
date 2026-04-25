
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}

    # Fetch all authors and prefetch active books
    authors = Author.objects.prefetch_related('book_set').all()

    # Create a list to hold author and their active books
    authors_with_books = []

    for author in authors:
        # Fetch active books for the current author
        books = author.book_set.filter(is_active=True)
        authors_with_books.append({
            'author': author,
            'books': books
        })

    _vars['authors_with_books'] = authors_with_books

    return render(request, 'template.html', _vars)
