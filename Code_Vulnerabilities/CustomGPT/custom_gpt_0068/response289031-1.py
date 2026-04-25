
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    # Use prefetch_related to optimize the query
    authors = Author.objects.prefetch_related('book_set').filter(is_active=True)

    # Prepare the context variable for the template
    _vars = {
        'authors': authors
    }

    # Render the template with authors and their books
    return render(request, 'template.html', _vars)
