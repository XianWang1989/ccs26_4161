
authors = Author.objects.prefetch_related('book_set').all()
