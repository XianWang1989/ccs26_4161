
def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()  # Pre-fetch related books

    # Optionally: Filter authors by active before fetching them
    active_authors = authors.filter(is_active=True)

    _vars['authors'] = active_authors

    return render(request, 'template.html', _vars)
