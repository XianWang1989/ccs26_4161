
def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Prepare a list to hold authors with their books
    authors_with_books = []

    # Loop through the authors
    for author in authors:
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')

        # Create a dictionary to hold author info and their books
        author_info = {
            'author': author,
            'books': books
        }
        authors_with_books.append(author_info)

    _vars['authors_with_books'] = authors_with_books

    return render(request, 'template.html', _vars)
