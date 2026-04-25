
def authors(request):
    _vars = {}
    authors = Author.objects.all().prefetch_related('book_set')  # Use related_name if set

    for author in authors:
        author.books = Book.objects.filter(author=author, is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
