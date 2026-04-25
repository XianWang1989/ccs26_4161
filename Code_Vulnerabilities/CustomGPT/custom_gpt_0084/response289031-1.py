
def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Iterate through the authors
    for author in authors:
        # Get active books related to the author
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')
        # Attach the books to the author
        author.books = books

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
