
def authors(request):
    _vars = {}
    authors = Author.objects.all()
    author_books = []

    # Loop through the authors
    for author in authors:
        # Fetch active books related to the author
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')

        # Append author and their corresponding books to the list
        author_books.append({
            'author': author,
            'books': books
        })

    _vars['author_books'] = author_books

    return render(request, 'template.html', _vars)
