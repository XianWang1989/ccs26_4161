
def authors(request):
    _vars = {}
    authors = Author.objects.all().prefetch_related('book_set')

    # Add an attribute to each author for their active books
    for author in authors:
        author.active_books = author.book_set.filter(is_active=True).order_by('-author__author_type__importance')

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
