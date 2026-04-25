
class FunctionWrapper:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self, row):
        # Prepare the arguments based on row and kwargs
        positional_args = [row[i] for i in self.args]
        # Include any static keyword arguments
        return self.func(*positional_args, **self.kwargs)

def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    elif isinstance(f, FunctionWrapper):
        return f(row)
    else:
        raise ValueError("Unsupported type for function f.")

# Example functions
def func1(x, y, z):
    return x + y + z

def func2(a, b=2):
    return a * b

# Function list using FunctionWrapper
fList = [
    FunctionWrapper(func1, 1, 0, 4),  # Passes row[1], row[0], row[4]
    FunctionWrapper(func2, 2, b=5),  # Passes row[2] and b=5
    'Hello, World',
    1  # Returns row[1]
]

# Example usage
row = [10, 20, 30, 40, 50]

for f in fList:
    result = foo(row, f)
    print(result)
