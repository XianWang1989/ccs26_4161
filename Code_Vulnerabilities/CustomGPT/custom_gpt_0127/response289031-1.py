
def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()  # Use prefetch_related to optimize queries

    for author in authors:
        # Fetch only active books for the current author
        books = author.book_set.filter(is_active=True).order_by('-author__author_type__importance')
        author.books = books  # Attach books to the author instance

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
