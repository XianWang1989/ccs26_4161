
def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()  # Prefetch related books

    # Add books to each author
    for author in authors:
        author.books = author.book_set.filter(is_active=True)  # Active books only

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
