
def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Loop through the authors
    for author in authors:
        # Fetching active books for each author
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')
        # Set a new attribute on the author instance to hold books
        author.books = books

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
