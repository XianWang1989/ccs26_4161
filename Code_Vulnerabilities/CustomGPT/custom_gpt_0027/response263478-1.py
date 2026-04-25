
class FunctionWrapper:
    def __init__(self, function, *args):
        self.function = function
        self.args = args

    def __call__(self, row):
        # Extract row elements as specified in args and combine with static args
        row_args = [row[i] for i in self.args if isinstance(i, int)]
        return self.function(*row_args)

# Example functions
def func1(a, b):
    return a + b

def func2(c):
    return c * 2

# Define the row and functions
row = [10, 20, 30, 40, 50]

fList = [
    FunctionWrapper(func1, 0, 1),  # Will pass row[0] and row[1] to func1
    FunctionWrapper(func2, 2),     # Will pass row[2] to func2
    "Hello, World!",
    2,
    FunctionWrapper(lambda x, y: x ** y, 3, 1)  # Pass row[3] and static 1
]

def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, (int, float)):
        return row[f]
    else:
        return f(row)

# Example usage
for f in fList:
    print(foo(row, f))
