
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all().prefetch_related('book_set')

    for author in authors:
        # Get active books for each author
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')
        author.books = books  # Attach books to the author instance

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
