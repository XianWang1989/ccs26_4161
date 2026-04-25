
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}

    # Prefetch related books for authors
    authors = Author.objects.prefetch_related('book_set').filter(is_active=True)

    # Filter books for each author after prefetching
    for author in authors:
        # Access active books through the reverse relation
        author.active_books = author.book_set.filter(is_active=True).order_by('-author_type__importance')

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
