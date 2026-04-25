
def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()  # Use prefetch_related for better performance

    for author in authors:
        # Filter active books directly within the author context
        author.active_books = author.book_set.filter(is_active=True)

    _vars['authors'] = authors

    return render(request, 'template.html', _vars)
