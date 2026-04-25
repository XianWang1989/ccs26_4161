
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all().prefetch_related('book_set')  # Use prefetch_related to optimize queries

    for author in authors:
        # Fetch active books for the author
        books = author.book_set.filter(is_active=True).order_by('-author_type__importance')

        # Adding books to the author object dynamically (or use a dictionary)
        author.books = books

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
