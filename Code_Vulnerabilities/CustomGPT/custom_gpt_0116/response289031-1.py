
def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()  # Prefetch related books

    # This will automatically include the related books for each author
    for author in authors:
        author.books = author.book_set.filter(is_active=True)  # Filter active books

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
