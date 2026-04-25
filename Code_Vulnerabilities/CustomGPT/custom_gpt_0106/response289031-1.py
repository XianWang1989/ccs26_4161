
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()  # Use `book_set` if that's your relation

    # restructuring authors to include books
    for author in authors:
        author.books = Book.objects.filter(author=author, is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
