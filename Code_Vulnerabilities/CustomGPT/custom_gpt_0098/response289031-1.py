
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()

    # Prepare a list to store author and their active books
    author_data = []

    for author in authors:
        # Get active books for each author
        books = author.book_set.filter(is_active=True).order_by('-author__author_type__importance')

        # Append author and their books to the list
        author_data.append({
            'author': author,
            'books': books
        })

    _vars['author_data'] = author_data

    return render(request, 'template.html', _vars)
