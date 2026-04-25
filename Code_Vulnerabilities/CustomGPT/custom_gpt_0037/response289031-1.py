
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()

    # Loop through the authors and attach the active books
    for author in authors:
        # Retrieve active books for each author
        author.active_books = Book.objects.filter(author=author.pk, is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
