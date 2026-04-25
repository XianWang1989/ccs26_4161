
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()  # Prefetch related books

    for author in authors:
        # Get active books for this author
        active_books = author.book_set.filter(is_active=True)
        author.active_books = active_books  # Add an attribute for easy access in the template

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
