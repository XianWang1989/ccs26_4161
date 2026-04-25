
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    # Prefetch related active books for each author
    authors = Author.objects.prefetch_related(
        'book_set'
    ).annotate(
        active_books_count=Count('book', filter=Q(book__is_active=True))
    ).filter(
        is_active=True
    )

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
