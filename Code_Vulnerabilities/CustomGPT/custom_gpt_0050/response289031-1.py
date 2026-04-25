
def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()  # Preload related books

    # Create a modified list of authors with their active books
    for author in authors:
        # Filter only the active books for each author
        author.active_books = author.book_set.filter(is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
