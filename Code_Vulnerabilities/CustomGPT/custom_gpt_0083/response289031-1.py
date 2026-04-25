
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()  # Optimize the query using prefetch_related

    for author in authors:
        # Fetch active books for each author
        active_books = author.book_set.filter(is_active=True).order_by('-author_type__importance')
        author.active_books = active_books  # Dynamically add active_books to the author instance

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
