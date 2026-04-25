
import logging

logger = logging.getLogger(__name__)

def authors(request):
    try:
        _vars = {}
        authors = Author.objects.prefetch_related('book_set').all()
        for author in authors:
            author.active_books = author.book_set.filter(is_active=True)

        _vars['authors'] = authors
        return render(request, 'template.html', _vars)
    except Exception as e:
        logger.error(f"Error fetching authors: {e}")
        return render(request, 'error_template.html', {'error': str(e)})
