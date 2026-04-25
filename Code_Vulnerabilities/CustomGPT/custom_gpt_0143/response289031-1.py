
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()

    for author in authors:
        # Get active books related to the author
        active_books = author.book_set.filter(is_active=True)
        # Add the active books to the author instance
        author.active_books = active_books

    _vars['authors'] = authors
    return render(request, 'template.html', _vars)
