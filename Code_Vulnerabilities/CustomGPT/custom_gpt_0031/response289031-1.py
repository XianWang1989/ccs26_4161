
def authors(request):
    _vars = {}
    # Get all active authors
    authors = Author.objects.filter(is_active=True)

    # Pre-fetch related books that are active
    for author in authors:
        author.books = author.book_set.filter(is_active=True).order_by('-author__author_type__importance')

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
