
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()  # Using prefetch_related to optimize the query

    # Create a list to store author data with their books
    author_list = []
    for author in authors:
        # Fetch active books for each author
        books = author.book_set.filter(is_active=True).order_by('-author_type__importance')

        # Append author and their books to the list
        author_list.append({
            'author': author,
            'books': books
        })

    _vars['authors'] = author_list  # Store the revised author list in the context

    return render(request, 'template.html', _vars)
