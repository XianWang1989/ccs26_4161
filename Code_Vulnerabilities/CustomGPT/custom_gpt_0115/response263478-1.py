
def foo(row, func, *args, **kwargs):
    # Prepare the arguments for the function
    func_args = [row[i] for i in kwargs.get('row_indices', [])] + list(args)
    return func(*func_args)
