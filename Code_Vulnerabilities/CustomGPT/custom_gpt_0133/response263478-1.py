
from functools import partial

def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    elif callable(f):
        return f(*[row[i] for i in range(len(row)) if i in f.indices] + [f.static_arg])
    elif isinstance(f, tuple) and callable(f[0]):
        func, indices, *static_args = f
        return func(*[row[i] for i in indices] + static_args)

# Example functions to use
def func1(a, b, static):
    return a + b + static

def func2(x):
    return x * 2

def func3(a, b):
    return f"{a} and {b}"

# Row data
row = [10, 20, 30, 40]

# Define your function list, where you can specify the indices to be passed
fList = [
    (func1, (0, 1), 5),   # Will take row[0] (10), row[1] (20), and add 5 => 35
    (func2, (1,)),        # Will take row[1] (20) => 40
    (func3, (2, 3)),      # Will take row[2] (30) and row[3] (40) => "30 and 40"
    'Hello, World',       # String example
    2                     # Will return row[2] => 30
]

# Applying the function list
for f in fList:
    result = foo(row, f)
    print(result)
