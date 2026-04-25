
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Pre-fetch related books for efficiency
    for author in authors:
        # Fetch active books related to the author
        books = Book.objects.filter(author=author, is_active=True).order_by('-author_type__importance')
        author.books = books  # Attach books to author

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
