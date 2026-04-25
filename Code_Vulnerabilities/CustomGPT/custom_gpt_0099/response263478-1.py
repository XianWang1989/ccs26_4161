
class FunctionWrapper:
    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def __call__(self, row):
        # Extract specific elements from the row based on positions
        extracted_args = [row[i] for i in self.args if isinstance(i, int)]
        # Add any static arguments
        return self.func(*extracted_args)

def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

def func3(a, b):
    return f"{a} and {b}"

# Define your function list using the wrapper
fList = [
    FunctionWrapper(func1, 1, 0, 4),
    FunctionWrapper(func2, 3),  # Passing index 3 from row
    FunctionWrapper(func3, 1, 2),  # Passing indices 1 and 2
    "Hello, World",
    2  # Just return the second element from the row
]

def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, (int, float)):
        return row[f]
    else:
        return f(row)

# Example row
row = [10, 20, 'spam', 5, 'eggs']

# Testing the FunctionList
results = [foo(row, f) for f in fList]
print(results)  # Output the results
