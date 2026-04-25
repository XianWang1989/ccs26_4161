
def foo(row, f, *args):
    if callable(f):
        # Extract specified elements from row
        row_args = [row[i] for i in args if isinstance(i, int)]
        return f(*row_args)
    else:
        return f  # Handle non-callable cases directly
