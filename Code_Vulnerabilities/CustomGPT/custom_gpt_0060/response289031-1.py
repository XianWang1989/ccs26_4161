
from django.shortcuts import render
from .models import Author, Book  # Adjust the import statements according to your project structure.

def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()  # Use prefetch_related for a reverse relationship

    # Loop through the authors and create a custom attribute for books
    for author in authors:
        # Filter active books related to the author and assign it to a new attribute
        author.active_books = Book.objects.filter(author=author, is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
