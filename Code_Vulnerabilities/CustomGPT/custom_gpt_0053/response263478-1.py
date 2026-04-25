
def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    elif callable(f):
        return f()  # Call without arguments for static functions
    else:
        func, *args = f
        resolved_args = [row[arg] if isinstance(arg, int) else arg for arg in args]
        return func(*resolved_args)

# Example functions
def func1(a, b):
    return a + b

def func2(x):
    return x * 2

def func3(a, b):
    return f"{a} and {b}"

# Example row
row = [5, 10, 15, 'spam', 'eggs']

# Improved fList
fList = [
    (func1, 1, 0),  # Using indices for row elements
    (func2, 2),     # Only one row element
    (func3, 'Hello', 'World'),  # Static arguments
    'Sample String',
    3  # Accessing the row element directly
]

# Testing the foo function
for f in fList:
    result = foo(row, f)
    print(result)
