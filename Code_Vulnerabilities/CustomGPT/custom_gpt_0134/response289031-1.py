
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').filter(is_active=True)

    # Create a list to store authors with their active books
    author_books = []

    for author in authors:
        # Fetch active books for this author
        books = author.book_set.filter(is_active=True)
        author_books.append({
            'author': author,
            'books': books
        })

    _vars['author_books'] = author_books

    return render(request, 'template.html', _vars)
