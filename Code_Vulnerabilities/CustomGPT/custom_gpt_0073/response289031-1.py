
def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Create a list to hold authors with their books
    author_books = []

    for author in authors:
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')

        # Create a dictionary to pair author and their active books
        author_books.append({
            'author': author,
            'books': books
        })

    _vars['author_books'] = author_books

    return render(request, 'template.html', _vars)
