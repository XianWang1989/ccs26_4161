
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Create a list to hold authors and their books
    author_list = []

    # Loop through each author
    for author in authors:
        # Get active books for each author
        books = Book.objects.filter(author=author, is_active=True)
        author_list.append({
            'author': author,
            'books': books,
        })

    _vars['authors'] = author_list  # Pass the list of authors with their books

    return render(request, 'template.html', _vars)
