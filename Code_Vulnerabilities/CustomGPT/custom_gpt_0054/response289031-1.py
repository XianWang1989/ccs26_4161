
from django.shortcuts import render
from django.db.models import Prefetch
from .models import Author, Book

def authors(request):
    _vars = {}

    # Prefetch books where is_active is True
    active_books = Book.objects.filter(is_active=True)
    authors = Author.objects.prefetch_related(Prefetch('book_set', queryset=active_books)).all()

    _vars['authors'] = authors
    return render(request, 'template.html', _vars)
