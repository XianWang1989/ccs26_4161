
def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Pre-fetch related books
    for author in authors:
        # Retrieve active books for the current author
        books = Book.objects.filter(
            author=author,
            is_active=True
        ).order_by('-author__author_type__importance')

        # Attach books to the author
        author.books = books  # Add an attribute `books` to the author

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
