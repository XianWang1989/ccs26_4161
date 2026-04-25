
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()  # Use prefetched relation

    # Loop through the authors
    for author in authors:
        author.books = author.book_set.filter(is_active=True)  # Assign active books to author

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
