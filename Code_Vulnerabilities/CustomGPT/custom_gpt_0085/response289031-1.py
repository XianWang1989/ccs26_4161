
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}

    # Use prefetch_related to get authors with their active books
    authors = Author.objects.prefetch_related(
        'book_set'
    ).all()

    # Filter out authors with their books
    for author in authors:
        author.active_books = author.book_set.filter(is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
