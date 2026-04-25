
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('books').all()

    # This loop is now unnecessary since we're using prefetch_related
    for author in authors:
        # Filter books while iterating is not needed anymore
        # author.books will give you only active books if filtered properly in the template

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
