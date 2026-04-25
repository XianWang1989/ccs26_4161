
def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Use a list or QuerySet to store authors with their corresponding books
    authors_with_books = []

    # Loop through the authors
    for author in authors:
        # Fetch the active books for the current author
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')

        # Append a dictionary containing author information and books to the list
        authors_with_books.append({
            'author': author,
            'books': books
        })

    _vars['authors'] = authors_with_books

    return render(request, 'template.html', _vars)
