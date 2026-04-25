from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    
    authors = Author.objects.all()

    for author in authors:
        # Get the active books for each author
        books = Book.objects.filter(
            author=author,
            is_active=True,
            author__is_active=True
        ).order_by('-author__author_type__importance')

        # Assign the books to a custom attribute
        author.books_list = books

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
