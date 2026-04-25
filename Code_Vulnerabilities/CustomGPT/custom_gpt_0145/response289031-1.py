
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}

    # Fetch all authors and their active books
    authors = Author.objects.prefetch_related('book_set').all()

    # Prepare a list to hold authors with their active books
    for author in authors:
        # Get active books for each author
        books = author.book_set.filter(is_active=True)

        # Attach books to author using a custom attribute
        author.active_books = books

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
