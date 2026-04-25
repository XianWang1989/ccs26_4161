
def authors(request):
    _vars = {}
    authors = Author.objects.all().prefetch_related('book_set').filter(is_active=True)

    for author in authors:
        # Filter the books related to each author that are active
        author.active_books = author.book_set.filter(is_active=True).order_by('-author_type__importance')

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
