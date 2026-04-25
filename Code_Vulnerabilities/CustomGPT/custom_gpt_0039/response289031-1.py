
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    authors = Author.objects.prefetch_related('book_set').all()  # Use prefetch_related for efficiency

    # Iterate through authors and filter active books
    for author in authors:
        author.books = author.book_set.filter(is_active=True)

    return render(request, 'template.html', {'authors': authors})
