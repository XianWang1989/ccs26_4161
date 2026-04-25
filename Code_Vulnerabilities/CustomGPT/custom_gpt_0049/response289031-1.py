
def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Loop through the authors
    for author in authors:
        # Retrieve active books for the author
        books = Book.objects.filter(author=author.pk, is_active=True).order_by('-author__author_type__importance')
        author.books = books  # Attach the list of books to the author object

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
