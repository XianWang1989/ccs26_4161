
def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()  # Use prefetch_related to fetch related books

    for author in authors:
        # Filtering the related books that are active
        author.books = author.book_set.filter(is_active=True).order_by('-author__author_type__importance')

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
