
class FuncWrapper:
    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def __call__(self, row):
        # Extract elements specified in args
        extracted_args = [row[i] if isinstance(i, int) else i for i in self.args]
        return self.func(*extracted_args)

def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, (int, float)):
        return row[f]
    elif isinstance(f, FuncWrapper):
        return f(row)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

# Example row of data
row = [10, 20, 30, "spam", "eggs"]

# Create function wrappers
fList = [
    FuncWrapper(func1, 0, 1, 2),          # func1 with elements at indexes 0, 1, 2
    FuncWrapper(func2, 3),                # func2 with element at index 3
    "Hello, World",                       # A string
    1                                      # An integer
]

# Using the functions
for f in fList:
    result = foo(row, f)
    print(result)
