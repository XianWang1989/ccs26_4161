
def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()

    for author in authors:
        # Filter active books directly using the related name
        author.active_books = author.book_set.filter(is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
