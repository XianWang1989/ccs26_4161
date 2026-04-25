
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()

    # Loop through authors and attach active books
    for author in authors:
        # Fetch active books for the current author
        author.active_books = author.book_set.filter(is_active=True).order_by('-author__author_type__importance')

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
