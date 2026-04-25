
from functools import partial

def foo(row, f):
    if callable(f):
        return f(**{k: row[i] for i, k in f.__code__.co_varnames.items() if k in row})
    elif isinstance(f, str):
        return f
    elif isinstance(f, (int, float)):
        return row[f]
    else:
        raise ValueError("Unsupported type in function list")

# Example functions
def func1(a, b, c):
    return a + b * c

def func2(x, y=10):
    return x * y

# Let's say we have a sample row
row = {'a': 2, 'b': 3, 'c': 4}

# Example function list using partial to bind the parameters
fList = [
    partial(func1, c=row['c']),
    partial(func2, y=5),
    "Hello, World",
    2
]

# Using the foo function
for f in fList:
    result = foo(row, f)
    print(result)
