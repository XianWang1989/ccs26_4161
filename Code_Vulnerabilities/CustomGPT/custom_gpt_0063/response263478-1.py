
from functools import partial

def foo(row, f):
    if callable(f):
        return f(*row)
    elif isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        raise ValueError("Unsupported type in f: {}".format(type(f)))

def custom_function(a, b, c, static_arg):
    return a + b + c + static_arg

# Example data row
row = [10, 20, 30, 5]

# fList with partial application for static arguments
fList = [
    partial(custom_function, static_arg=100),
    lambda x: x[0] * 2,  # Example lambda function
    "Hello, World",
    1  # Accessing row index
]

# Example usage of foo
for f in fList:
    result = foo(row, f)
    print(result)
