
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    # Prefetch active books related to authors
    authors = Author.objects.prefetch_related(
        'book_set'  # assuming the related name for books is 'book_set'
    ).filter(is_active=True)

    for author in authors:
        # Filter books that are active for the current author
        author.books = [book for book in author.book_set.all() if book.is_active]

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
