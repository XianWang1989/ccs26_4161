
def authors(request):
    _vars = {}
    authors = Author.objects.all()

    for author in authors:
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')
        author.books = books  # Adding books to the author instance

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
