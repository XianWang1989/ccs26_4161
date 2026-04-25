
def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()  # Prefetch related books

    for author in authors:
        # Filter only active books
        author.books = author.book_set.filter(is_active=True)  # Assign active books to the author

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
