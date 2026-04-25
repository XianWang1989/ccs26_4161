
def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()  # Use prefetch_related

    for author in authors:
        # Filter books directly based on related set
        books = author.book_set.filter(is_active=True)
        author.books = books  # Attach books to the author instance

    _vars['authors'] = authors
    return render(request, 'template.html', _vars)
