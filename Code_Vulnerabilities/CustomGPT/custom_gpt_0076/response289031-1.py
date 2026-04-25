
def authors(request):
    _vars = {}

    # Get all authors and annotate with their active books
    authors = Author.objects.prefetch_related(
        'book_set'  # Assuming reverse relation from Book to Author is 'book_set'
    ).all()

    # Now we filter active books when rendering
    for author in authors:
        author.books = author.book_set.filter(is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
