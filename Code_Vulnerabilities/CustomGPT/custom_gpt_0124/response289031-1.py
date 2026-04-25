
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Create a list to hold authors with their books
    author_data = []

    # Loop through each author to find their active books
    for author in authors:
        books = Book.objects.filter(author=author, is_active=True).order_by('-author_type__importance')
        author_data.append({
            'author': author,
            'books': books
        })

    _vars['author_data'] = author_data

    return render(request, 'template.html', _vars)
