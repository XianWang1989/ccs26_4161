
def foo(row, f, *args, **kwargs):
    if callable(f):
        # Collect the necessary row elements based on the indices in kwargs
        row_args = [row[i] for i in kwargs.get('indices', [])]
        # Call the function with row arguments plus any static arguments
        return f(*row_args, *args)
    elif isinstance(f, str):
        return f
    elif isinstance(f, (int, float)):
        return row[f]
    else:
        raise ValueError("Invalid function type")

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x ** 2

# Example usage
row = [10, 20, 30, 40, 50]
fList = [
    (func1, {'indices': [0, 1, 2]}, 5),  # Use row[0], row[1], row[2] plus static argument 5
    (func2, {'indices': [3]}),           # Use row[3]
    'Hello, World',
    1                                    # Use row[1]
]

# Calling the functions from fList
for f, kwargs in fList:
    if isinstance(f, tuple):
        print(foo(row, f[0], **f[1]))  # Unpack the tuple elements for foo
    else:
        print(foo(row, f))
