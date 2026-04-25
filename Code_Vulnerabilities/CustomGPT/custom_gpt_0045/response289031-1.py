
def authors(request):
    _vars = {}
    # Retrieve all authors
    authors = Author.objects.all().prefetch_related('book_set')

    # Prepare a list to hold authors with their active books
    author_books = []

    for author in authors:
        # Get the active books for each author
        books = author.book_set.filter(is_active=True).order_by('-author__author_type__importance')

        # Create a dictionary to represent each author and their books
        author_books.append({
            'author': author,
            'books': books
        })

    _vars['author_books'] = author_books

    return render(request, 'template.html', _vars)
