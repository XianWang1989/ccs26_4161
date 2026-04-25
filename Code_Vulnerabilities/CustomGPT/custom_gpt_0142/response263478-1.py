
def foo(row, f, *args, **kwargs):
    """Evaluate the function 'f' with specific elements from 'row' and additional arguments."""

    if callable(f):  # Check if f is a callable function
        # Extract specified elements from 'row' using kwargs
        row_args = [row[i] for i in kwargs.get('indices', [])]
        return f(*row_args, *args)  # Call f with elements from row, additional args
    elif isinstance(f, str):  # If f is a string, return it
        return f
    elif isinstance(f, int):  # If f is an int, return the corresponding element from row
        return row[f]
    else:
        raise ValueError("Invalid function or type provided.")

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x, y):
    return x * y

# Using the modified foo function
row_data = [10, 20, 30, 40, 50]

# Example fList
fList = [
    (func1, {'indices': [0, 1, 2]}),  # Pass elements at indices 0, 1, and 2 to func1
    (func2, {'indices': [1, 3]}),      # Pass elements at indices 1 and 3 to func2
    'Hello, World',                     # Static string
    2                                   # An integer to directly access the row
]

# Test calls
for f in fList:
    if isinstance(f, tuple):
        result = foo(row_data, f[0], **f[1])
    else:
        result = foo(row_data, f)
    print(result)
