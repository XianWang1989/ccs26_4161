
def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Loop through the authors and create a list of items containing the author and their books
    authors_with_books = []
    for author in authors:
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')
        authors_with_books.append({
            'author': author,
            'books': books
        })

    _vars['authors_with_books'] = authors_with_books

    return render(request, 'template.html', _vars)
