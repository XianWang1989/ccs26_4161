
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all().prefetch_related('book_set')  # Use prefetch_related to optimize queries

    # Create a list to hold authors with their books
    authors_with_books = []

    for author in authors:
        # Filter active books for each author
        books = Book.objects.filter(author=author, is_active=True)
        author.books = books  # Attach the books to the author instance
        authors_with_books.append(author)

    _vars['authors'] = authors_with_books

    return render(request, 'template.html', _vars)
