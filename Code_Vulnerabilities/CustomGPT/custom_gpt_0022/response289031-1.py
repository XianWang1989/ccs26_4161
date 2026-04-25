
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()

    # Loop through authors and filter their active books
    for author in authors:
        books = author.book_set.filter(is_active=True)
        author.books = books  # Attach the filtered books

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
