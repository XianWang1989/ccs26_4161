
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
