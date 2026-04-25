
def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    elif callable(f):
        return f()
    elif isinstance(f, tuple):
        func = f[0]
        args = [row[i] if isinstance(i, int) else i for i in f[1]]
        return func(*args)

# Example functions
def func1(a, b):
    return a + b

def func2(x):
    return x * 2

def func3(a, b):
    return f"{a} and {b}"

# Redefining fList
fList = [
    (func1, [1, 0]),  # Passing elements from row
    (func2, [2]),     # Using the row element at index 2
    (func3, ['spam', 'eggs']),  # Static arguments
    'Hello, World',
    2
]

# Sample row
row = [10, 20, 30, 40]

# Testing foo with various elements
for f in fList:
    print(foo(row, f))
