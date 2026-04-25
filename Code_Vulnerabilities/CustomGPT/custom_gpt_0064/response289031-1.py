
def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Create a list to hold authors with their books
    author_books = []

    # Loop through the authors
    for author in authors:
        # Get active books for this author
        books = Book.objects.filter(author=author, is_active=True)
        author_books.append({
            'author': author,
            'books': books
        })

    _vars['author_books'] = author_books

    return render(request, 'template.html', _vars)
