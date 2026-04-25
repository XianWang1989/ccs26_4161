
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    authors = Author.objects.all().prefetch_related('book_set')

    for author in authors:
        # Get active books for each author
        author.books = author.book_set.filter(is_active=True)

    context = {
        'authors': authors
    }

    return render(request, 'template.html', context)
