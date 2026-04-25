
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()

    for author in authors:
        # Get active books for this author
        author.books = author.book_set.filter(is_active=True).order_by('-author_type__importance')

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
