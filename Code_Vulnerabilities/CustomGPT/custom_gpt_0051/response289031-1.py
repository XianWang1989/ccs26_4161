
def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Pre-load related books using select_related or prefetch_related for efficiency
    authors_with_books = []

    for author in authors:
        books = Book.objects.filter(author=author, is_active=True)
        authors_with_books.append({
            'author': author,
            'books': books
        })

    _vars['authors_with_books'] = authors_with_books

    return render(request, 'template.html', _vars)
