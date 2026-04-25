
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    # Use prefetch_related to get all active books for active authors
    authors = Author.objects.prefetch_related(
        'book_set'  # Assuming the related name for the Book model is 'book_set'
    ).filter(is_active=True)

    # Filter the books to only include active ones
    for author in authors:
        author.active_books = author.book_set.filter(is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
