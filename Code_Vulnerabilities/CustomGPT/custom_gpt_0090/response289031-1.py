
def authors(request):
    _vars = {}
    authors = Author.objects.all().prefetch_related('book_set')

    for author in authors:
        # Filter for active books only, using the related manager
        author.books = author.book_set.filter(is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
