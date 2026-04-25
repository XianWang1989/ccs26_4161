
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    # Use prefetch_related to fetch the related books more efficiently
    authors = Author.objects.prefetch_related(
        'book_set'
    ).all()

    # Filter the books for each author
    for author in authors:
        # Get only active books for this author
        author.active_books = author.book_set.filter(is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
