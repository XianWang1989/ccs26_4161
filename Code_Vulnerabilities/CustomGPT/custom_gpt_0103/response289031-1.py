
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    # Fetch all authors and use select_related for related objects
    authors = Author.objects.prefetch_related('book_set').all()

    # Get active books for each author
    for author in authors:
        author.active_books = author.book_set.filter(is_active=True)

    context = {
        'authors': authors
    }

    return render(request, 'template.html', context)
