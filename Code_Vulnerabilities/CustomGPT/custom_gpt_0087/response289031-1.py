
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()

    # Prepare the authors with their active books
    for author in authors:
        author.books = author.book_set.filter(is_active=True)

    _vars['authors'] = authors
    return render(request, 'template.html', _vars)
