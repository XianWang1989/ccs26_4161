
def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()  # Use related name for Books

    # Loop through authors and filter their books
    for author in authors:
        # Directly access related books using the related manager
        author.active_books = author.book_set.filter(is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
