
def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()

    # Create a dictionary to hold authors and their active books
    for author in authors:
        # Get the active books for each author
        author.active_books = author.book_set.filter(is_active=True).order_by('-author_type__importance')

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
