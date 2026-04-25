
class FunctionWrapper:
    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def evaluate(self, row):
        # Extract specified elements from row based on indices in args
        row_args = [row[i] for i in self.args if isinstance(i, int)]  # get elements from row
        static_args = [i for i in self.args if not isinstance(i, int)]  # static elements
        return self.func(*row_args, *static_args)

def foo(row, f):
    if isinstance(f, FunctionWrapper):
        return f.evaluate(row)
    elif isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        raise ValueError("Unsupported type provided to foo")

# Example functions to demonstrate usage
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

# Example data row
row_data = [10, 20, 30, 40]

# Creating function wrappers
fList = [
    FunctionWrapper(func1, 0, 1, 2),  # Uses elements at indices 0, 1, 2 of the row
    FunctionWrapper(func2, 3),       # Uses element at index 3 of the row
    'Hello, World',
    1
]

# Usage
for f in fList:
    print(foo(row_data, f))  # Outputs the results of each function call or the string
