
class FunctionWrapper:
    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def __call__(self, row):
        # Extract variables from row using indices
        arguments = [row[i] for i in self.args if isinstance(i, int)] + \
                    [i for i in self.args if not isinstance(i, int)]
        return self.func(*arguments)

# Example functions
def func1(a, b, c):
    return a + b * c

def func2(x):
    return x ** 2

# Sample fList
fList = [
    FunctionWrapper(func1, 1, 0, 4),  # row[1], row[0], static 4
    FunctionWrapper(func2, 2),       # row[2]
    'Hello, World',
    2
]

# Revised foo function
def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, (int, float)):
        return row[f]  # Handle static integers for row access
    else:
        return f(row)  # Call the callable wrapper

# Usage example
row = [5, 10, 3, 7]  # Example row
results = [foo(row, f) for f in fList]
print(results)
