
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}

    # Fetch all authors with their active books
    authors_with_books = Author.objects.prefetch_related(
        'book_set'
    ).filter(is_active=True)

    # Iterate over authors and their books
    for author in authors_with_books:
        author.books = author.book_set.filter(is_active=True)

    _vars['authors'] = authors_with_books

    return render(request, 'template.html', _vars)
