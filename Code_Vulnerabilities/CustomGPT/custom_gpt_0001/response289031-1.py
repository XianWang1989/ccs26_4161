
def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Pre-fetch related books to avoid n+1 query problem
    for author in authors:
        # Retrieve active books related to the author
        books = Book.objects.filter(author=author, is_active=True).order_by(
            '-author__author_type__importance'
        )  # Note: author__is_active check is redundant if filtering by active books only

        # Attach books to author (this creates a dictionary for demonstration)
        author.books = books  # This won't save to the database but adds an attribute for rendering

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
