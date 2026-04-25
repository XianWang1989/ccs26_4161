
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    # Use prefetch_related to fetch related books
    authors = Author.objects.prefetch_related('book_set').all()

    # Filter books directly in the template if necessary
    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
