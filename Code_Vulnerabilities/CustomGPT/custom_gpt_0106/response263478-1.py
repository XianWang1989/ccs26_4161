
class FunctionWrapper:
    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def __call__(self, row):
        # Replace elements in self.args with values from row
        resolved_args = [arg if not isinstance(arg, str) else row[int(arg)] for arg in self.args]
        return self.func(*resolved_args)

def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        return f(row)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

# Creating a function list
fList = [
    FunctionWrapper(func1, '1', 0, 4),  # passing 1st index, 0th index, and static 4
    FunctionWrapper(func2, 10)          # passing static 10
]

# Example row
row = [5, 2, 3, 4, 10]

# Using foo
for f in fList:
    print(foo(row, f))  # Outputs: 7, 20
