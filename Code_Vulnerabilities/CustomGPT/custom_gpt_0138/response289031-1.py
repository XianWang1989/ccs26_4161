
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Loop through the authors and annotate with their active books
    for author in authors:
        author.books = Book.objects.filter(author=author, is_active=True).order_by('-author_type__importance')

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
