
def authors(request):
    _vars = {}
    authors = Author.objects.prefetch_related('book_set').all()

    # Create a list to hold author data with their books
    author_data = []

    # Loop through the authors
    for author in authors:
        # Filter books related to the current author
        books = author.book_set.filter(is_active=True).order_by('-author_type__importance')
        author_data.append({
            'author': author,
            'books': books
        })

    _vars['authors'] = author_data

    return render(request, 'template.html', _vars)
