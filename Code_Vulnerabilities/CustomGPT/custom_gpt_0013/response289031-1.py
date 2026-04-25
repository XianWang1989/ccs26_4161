
def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()

    # Annotate authors with their active books
    for author in authors:
        author.books = author.book_set.filter(is_active=True)  # Use related name for books

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
