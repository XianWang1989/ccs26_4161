
def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()

    for author in authors:
        # Retrieve active books related to the author
        books = author.book_set.filter(is_active=True).order_by('-author_type__importance')
        author.books = books  # Adding a custom attribute

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
