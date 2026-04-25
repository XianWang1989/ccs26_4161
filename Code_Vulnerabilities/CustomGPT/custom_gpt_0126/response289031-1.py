
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    # Fetch all authors along with their active books in one query
    authors = Author.objects.prefetch_related(
        'book_set'
    ).filter(is_active=True)

    # Filter out only active books for each author in the template
    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
