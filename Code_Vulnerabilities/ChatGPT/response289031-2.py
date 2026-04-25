
from django.shortcuts import render
from .models import Author, Book

def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('books').all()  # Prefetch books for all authors

    # Now you can simply access books as a related_name on the author instance
    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
