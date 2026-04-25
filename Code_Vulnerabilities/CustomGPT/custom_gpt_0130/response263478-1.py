
def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    elif callable(f[0]):
        func = f[0]
        indices = f[1]
        static_args = f[2] if len(f) > 2 else []
        args = [row[i] for i in indices] + static_args
        return func(*args)

# Example functions
def func1(x, y):
    return x + y

def func2(x, y, z):
    return x * y + z

# Function list
fList = [
    (func1, [1, 0], [5]),  # func1 with elements from row[1] and row[0], plus 5
    (func2, [0, 2], []),   # func2 with elements from row[0] and row[2], no static arguments
    'Hello, World',
    2
]

# Example row
row = [10, 20, 30, 40]

# Using foo
for f in fList:
    result = foo(row, f)
    print(result)
