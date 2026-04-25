
def authors(request):
    _vars = {}
    authors = Author.objects.all().prefetch_related('book_set').filter(is_active=True)

    author_list = []

    # Loop through authors
    for author in authors:
        # Get all active books for the current author
        books = author.book_set.filter(is_active=True).order_by('-author_type__importance')
        author_list.append({
            'author': author,
            'books': books,
        })

    _vars['authors'] = author_list

    return render(request, 'template.html', _vars)
