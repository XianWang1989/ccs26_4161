
def foo(row, f, *args):
    if callable(f):
        # Use the row and static arguments passed to f
        return f(*args, *[row[i] for i in args if isinstance(i, int)])
    elif isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        raise ValueError("Unsupported type for f")

# Example functions
def func1(x, y):
    return x + y

def func2(a, b):
    return a * b

# fList with more structured data
fList = [
    (func1, (0, 1)),  # indices from row
    (func2, (2, 3)),  # indices from row
    'Hello, World',
    2  # pulls the element at index 2 from row
]

# Sample row
row = [10, 20, 3, 5]

# Using the `foo` function
for item in fList:
    if isinstance(item, tuple):
        function, indices = item
        result = foo(row, function, *indices)
        print(result)
    else:
        print(foo(row, item))
