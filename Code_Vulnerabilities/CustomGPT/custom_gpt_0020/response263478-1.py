
from functools import partial

class FunctionWrapper:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self, row):
        # Extract the specified elements from the row using args.
        # Use kwargs to include any additional static arguments.
        selected_args = [row[i] for i in self.args]
        return self.func(*selected_args, **self.kwargs)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

def func3(param1, param2):
    return f"{param1} and {param2}"

# Specifying functions using FunctionWrapper
fList = [
    FunctionWrapper(func1, 1, 0, 4),  # Pass row[1], row[0], row[4]
    FunctionWrapper(func2, 2),        # Pass row[2]
    FunctionWrapper(func3, 0, 1, static_param='static_value')  # Pass row[0], row[1]
]

def foo(row, f):
    if isinstance(f, FunctionWrapper):
        return f(row)
    else:
        return f  # For other cases like strings or integers

# Test data
row = [10, 20, 30, 40, 50]

# Using the foo function with the function list
for f in fList:
    result = foo(row, f)
    print(result)
