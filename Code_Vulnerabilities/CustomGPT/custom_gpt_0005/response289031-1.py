
def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()

    for author in authors:
        # Filter active books for the author
        author.books = author.book_set.filter(is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
