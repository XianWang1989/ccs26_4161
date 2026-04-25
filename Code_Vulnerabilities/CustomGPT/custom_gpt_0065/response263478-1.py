
def foo(row, f):
    # If f is a string, return it directly
    if isinstance(f, str):
        return f
    # If f is an integer, return the element at that index in row
    elif isinstance(f, int):
        return row[f]
    # If f is callable, unpack arguments
    elif callable(f):
        return f(*args)

def call_function(f, row):
    # Extract arguments for the function
    args = []
    if isinstance(f, tuple):
        func, *args = f  # Unpacking function and its arguments
    elif isinstance(f, list):
        # Handle list for partial static args
        func = args.pop(0)  # First element should be the function
        args = args  # The rest are arguments

    # Resolve arguments from row
    resolved_args = [row[i] if isinstance(i, int) else i for i in args]
    return foo(row, func)(*resolved_args)

# Example functions
def func1(a, b):
    return a + b

def func2(a):
    return a * 2

# Example fList
fList = [
    (func1, 1, 0),  # Function with specific indices
    (func2, 4),     # Function with one index
    'Hello, World', # Static string
    2               # Integer index
]

# Example row
row = [10, 20, 30, 40, 50]

# Usage
for f in fList:
    print(call_function(f, row))
