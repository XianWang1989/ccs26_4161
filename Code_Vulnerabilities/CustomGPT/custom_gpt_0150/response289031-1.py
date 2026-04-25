
def authors(request):
    _vars = {}
    authors = Author.objects.all()

    # Create a list to hold author data with their books
    author_data = []

    # Loop through the authors
    for author in authors:
        # Fetch active books for the current author
        books = Book.objects.filter(author=author, is_active=True).order_by('-author__author_type__importance')

        # Append author data and books to the list
        author_data.append({
            'author': author,
            'books': books
        })

    _vars['author_data'] = author_data

    return render(request, 'template.html', _vars)
