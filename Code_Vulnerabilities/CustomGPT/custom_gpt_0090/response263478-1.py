
from functools import partial

def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    elif callable(f):
        return f(*[row[i] for i in f.__code__.co_varnames if i in row])
    elif isinstance(f, tuple) and callable(f[0]):
        func, indices = f
        return func(*[row[i] for i in indices])
    else:
        raise ValueError("Unsupported function type")

# Example functions
def func1(a, b):
    return a + b

def func2(x):
    return x * x

# Example row
row = [10, 20, 30, 40]

# Example fList
fList = [
    (func1, (0, 1)),  # will sum row[0] and row[1]
    (func2, (1,)),    # will square row[1]
    "Hello, World",
    2,                # will return row[2]
]

# Usage
for f in fList:
    print(foo(row, f))
