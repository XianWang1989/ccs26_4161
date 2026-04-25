
def authors(request):
    _vars = {}
    authors = Author.objects.all().prefetch_related('book_set')

    # Create a list to hold the authors with their active books
    authors_with_books = []

    for author in authors:
        # Fetch only active books for the current author
        active_books = author.book_set.filter(is_active=True).order_by('-author_type__importance')
        authors_with_books.append({
            'author': author,
            'books': active_books
        })

    _vars['authors'] = authors_with_books

    return render(request, 'template.html', _vars)
