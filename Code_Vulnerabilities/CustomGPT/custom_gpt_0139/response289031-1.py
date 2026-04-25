
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}

    # Using prefetch_related for better performance
    authors = Author.objects.prefetch_related(
        'book_set').filter(is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
