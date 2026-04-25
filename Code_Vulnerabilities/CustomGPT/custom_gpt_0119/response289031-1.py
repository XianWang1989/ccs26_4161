
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}

    # Fetching authors with their active books
    authors = Author.objects.prefetch_related(
        'book_set'
    ).annotate(
        active_books_count=Count('book', filter=Q(book__is_active=True))
    )

    # Adding active books to each author
    for author in authors:
        author.active_books = author.book_set.filter(is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
