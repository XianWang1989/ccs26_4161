
def authors(request):
    _vars = {}
    authors = Author.objects.all().prefetch_related('book_set')

    # Prepare a list to hold authors with their active books
    author_data = []
    for author in authors:
        books = author.book_set.filter(is_active=True).order_by('-author_type__importance')
        author_data.append({
            'author': author,
            'books': books
        })

    _vars['authors'] = author_data

    return render(request, 'template.html', _vars)
