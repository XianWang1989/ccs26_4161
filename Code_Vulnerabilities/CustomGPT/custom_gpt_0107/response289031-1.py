
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()  # Use prefetch_related to optimize queries

    for author in authors:
        # Fetch active books for the current author
        active_books = author.book_set.filter(is_active=True)  # No need to repeat author lookup here
        author.active_books = active_books  # Attach the books to the author object

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
