
def authors(request):
    _vars = {}

    # Retrieve all authors
    authors = Author.objects.prefetch_related('book_set').all()

    # Iterate through the authors
    for author in authors:
        # Filter the related books for active ones
        author.active_books = author.book_set.filter(is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
