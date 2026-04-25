
def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Create a list to hold data with authors and their books
    author_data = []

    # Loop through the authors
    for author in authors:
        books = Book.objects.filter(author=author, is_active=True).select_related('author__author_type').order_by('-author__author_type__importance')
        author_data.append({
            'author': author,
            'books': books
        })

    _vars['author_data'] = author_data

    return render(request, 'template.html', _vars)
