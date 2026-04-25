
class FunctionWrapper:
    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def __call__(self, row):
        # Extract elements from row based on specified indices
        row_args = [row[i] for i in self.args if isinstance(i, int)]
        # Static arguments will be included
        return self.func(*row_args)

# Example functions
def func1(a, b, c):
    return a + b * c

def func2(x):
    return x ** 2

# Example fList using FunctionWrapper
fList = [
    FunctionWrapper(func1, 1, 0, 4),  # Access row[1], row[0], static 4
    FunctionWrapper(func2, 3),        # Access row[3]
    "Hello, World",
    2                                   # Directly returning a value
]

def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    elif isinstance(f, FunctionWrapper):
        return f(row)
    else:
        raise TypeError("Unsupported type in function list")

# Example usage
row_data = [10, 20, 30, 40, 50]
for f in fList:
    print(foo(row_data, f))
