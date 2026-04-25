
def authors(request):
    _vars = {}
    authors = Author.objects.all().prefetch_related('book_set')

    # Prepare a list to store authors along with their active books
    author_list = []

    # Loop through the authors
    for author in authors:
        # Find the active books for each author
        books = author.book_set.filter(is_active=True)

        # Append the author and their books to the list
        author_list.append({
            'author': author,
            'books': books
        })

    _vars['author_list'] = author_list

    return render(request, 'template.html', _vars)
