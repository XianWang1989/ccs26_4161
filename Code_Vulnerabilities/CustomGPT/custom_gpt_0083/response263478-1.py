
from functools import partial

def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    elif callable(f):  # If f is a function
        return f()
    elif isinstance(f, tuple) and len(f) > 0:
        func = f[0]
        args = []
        for arg in f[1:]:
            if isinstance(arg, int):
                args.append(row[arg])
            elif callable(arg):
                args.append(arg())  # Call the function if it's callable
            else:
                args.append(arg)  # Add static arguments directly
        return func(*args)
    else:
        raise ValueError("Unsupported format for function specification")

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

# Example fList
fList = [
    (func1, 1, 0, 'constant_value'),  # Uses row[1], row[0], and a static value
    (func2, 3),                        # Uses row[3]
    "Hello, World",
    2
]

# Example row
row = [10, 20, 30, 40, 50]

# Using the functions
for f in fList:
    result = foo(row, f)
    print(result)
