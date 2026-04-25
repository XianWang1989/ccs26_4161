
from functools import partial

def foo(row, func_spec):
    if isinstance(func_spec, tuple):
        func = func_spec[0]
        indices = func_spec[1]
        return func(*(row[i] for i in indices))
    elif callable(func_spec):
        return func_spec(row)  # Allow direct function calls
    else:
        return func_spec  # Return static values directly

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

# Example dataset row
row = [10, 20, 30, 40, 50]

# Function specifications
fList = [
    (func1, [0, 1, 2]),         # sums elements at indices 0, 1, 2
    (func2, [3]),               # applies func2 to element at index 3
    'Hello, World',             # static string
    2                           # static integer
]

# Testing the foo function
for f in fList:
    result = foo(row, f)
    print(result)
