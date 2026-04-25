
def foo(row, f, *static_args):
    if callable(f):
        return f(*(static_args + [row[i] for i in f.indices]))
    return f

class FuncRef:
    def __init__(self, func, *indices):
        self.func = func
        self.indices = indices

    def __call__(self, *args):
        return self.func(*args)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x, y):
    return x * y

# Function list
fList = [
    FuncRef(func1, 1, 0, 4),
    FuncRef(func2, 2, 3),
    "Hello, World",
    42
]

# Example row
row = [10, 20, 30, 40, 50]

# Using the foo function
for f in fList:
    result = foo(row, f)
    print(result)
