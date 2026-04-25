
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}

    # Use prefetch_related to fetch authors and their active books
    authors = Author.objects.prefetch_related(
        'book_set'  # Assuming related name for Book FK in Author is 'book_set'
    ).all()

    # Filter out inactive books in the template or just prefetch active ones
    for author in authors:
        author.active_books = author.book_set.filter(is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
