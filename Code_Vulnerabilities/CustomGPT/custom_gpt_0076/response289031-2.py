
import logging

def authors(request):
    _vars = {}
    try:
        authors = Author.objects.prefetch_related('book_set').all()
        for author in authors:
            author.books = author.book_set.filter(is_active=True)
        _vars['authors'] = authors
    except Exception as e:
        logging.error("Error fetching authors: %s", e)
        # Handle the error appropriately
        _vars['error'] = "An error occurred while fetching authors."

    return render(request, 'template.html', _vars)
