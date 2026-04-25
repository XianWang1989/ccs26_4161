
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all().prefetch_related('book_set')

    for author in authors:
        # Get active books for each author
        active_books = author.book_set.filter(is_active=True)
        author.active_books = active_books  # Attach active books to the author instance

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
