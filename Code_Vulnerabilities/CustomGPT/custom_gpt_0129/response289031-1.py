
def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Create a list to store authors with their corresponding active books
    authors_with_books = []

    # Loop through the authors
    for author in authors:
        # Get active books for each author
        books = Book.objects.filter(author=author, is_active=True)

        # Append a dictionary of author and their books to the list
        authors_with_books.append({
            'author': author,
            'books': books
        })

    _vars['authors_with_books'] = authors_with_books

    return render(request, 'template.html', _vars)
