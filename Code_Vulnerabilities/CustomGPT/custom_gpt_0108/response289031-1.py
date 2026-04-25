
def authors(request):
    _vars = {}
    # Fetch all authors and prefetch related active books
    authors = Author.objects.prefetch_related(
        'book_set'
    ).all()

    # Filter authors with their books directly
    for author in authors:
        author.active_books = author.book_set.filter(is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
