
def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()

    for author in authors:
        # Filter books related to the author
        author.books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')

    _vars['authors'] = authors
    return render(request, 'template.html', _vars)
