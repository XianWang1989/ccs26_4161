
def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Loop through the authors
    for author in authors:
        # Get active books for the author
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')
        author.books = books  # Create a custom attribute

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
