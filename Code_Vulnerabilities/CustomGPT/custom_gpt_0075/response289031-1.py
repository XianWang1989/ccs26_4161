
def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Add a list of active books to each author
    for author in authors:
        books = Book.objects.filter(author=author, is_active=True)
        author.books = books  # Attach books to the author object

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
