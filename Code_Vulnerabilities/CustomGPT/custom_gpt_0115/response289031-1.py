
def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Loop through the authors and get their active books
    for author in authors:
        # Get active books for this author
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')
        # Attach the books to the author instance (if you want a custom property)
        author.books = books

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
