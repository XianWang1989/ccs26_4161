
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()

    # Prepare a list to hold the authors and their active books
    author_books = []

    # Loop through the authors
    for author in authors:
        # Get the active books for the author
        books = author.book_set.filter(is_active=True).order_by('-author_type__importance')

        author_books.append({
            'author': author,
            'books': books
        })

    _vars['author_books'] = author_books
    return render(request, 'template.html', _vars)
