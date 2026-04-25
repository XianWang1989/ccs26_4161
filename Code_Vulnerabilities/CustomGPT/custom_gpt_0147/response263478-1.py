
class FunctionWrapper:
    def __init__(self, func, indices=None, *args):
        self.func = func
        self.indices = indices if indices is not None else []
        self.static_args = args

    def __call__(self, row):
        # Gather arguments from the row based on indices
        row_args = [row[i] for i in self.indices]
        # Call the function with both row args and static args
        return self.func(*row_args, *self.static_args)

def foo(row, f):
    return f(row)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x, y):
    return x * y

# Creating an fList with instances of FunctionWrapper
fList = [
    FunctionWrapper(func1, [1, 0, 4]),  # Uses elements 1, 0, 4 from the row
    FunctionWrapper(func2, [0, 2], 10),  # Uses elements 0, 2 from the row and a static arg
    "Hello, World",
    2  # To access an element from the row directly
]

# Using the `foo` function
row_data = [5, 10, 3, 7, 8]  # Example row

# Test the fList
for f in fList:
    if isinstance(f, FunctionWrapper):
        print(foo(row_data, f))  # Calls the wrapped function
    elif isinstance(f, str):
        print(f)  # Just return the string
    elif isinstance(f, int):
        print(row_data[f])  # Access from the row
