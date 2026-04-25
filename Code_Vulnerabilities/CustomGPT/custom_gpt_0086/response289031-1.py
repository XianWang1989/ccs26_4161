
def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()

    # Prepare authors list with their active books
    for author in authors:
        # Fetch active books associated with the author
        author.active_books = author.book_set.filter(is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
