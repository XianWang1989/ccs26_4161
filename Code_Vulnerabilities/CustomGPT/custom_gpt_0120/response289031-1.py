
def authors(request):
    _vars = {}

    # Retrieve all authors
    authors = Author.objects.all()

    # Prepare a list to store authors with their books
    authors_with_books = []

    # Loop through the authors
    for author in authors:
        # Get active books for the current author
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')

        # Append author and their books to the list
        authors_with_books.append({
            'author': author,
            'books': books
        })

    _vars['authors_with_books'] = authors_with_books

    return render(request, 'template.html', _vars)
