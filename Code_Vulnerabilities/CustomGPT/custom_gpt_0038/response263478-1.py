
def flexible_wrapper(f, *args, **kwargs):
    return f(*args, **kwargs)

def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    elif callable(f):
        return f(row)
    elif isinstance(f, tuple):
        func, *params = f
        # Prepare arguments: includes row elements and static args
        args = {k: row[v] for k, v in params if isinstance(v, int)}
        return func(**args)
    else:
        raise ValueError("Unsupported type in function list")

# Example functions
def func1(x, y):
    return x + y

def func2(a, b):
    return a * b

# Example data row
row = [10, 20, 30, 40, 50]

# Function list
fList = [
    (func1, {'x': 1, 'y': 0}),  # will take row[1] and row[0]
    (func2, {'a': 2, 'b': 3}),  # will take constants 2 and 3
    'Hello, World',  # simply return the string
    2  # will return row[2]
]

# Example usage
for f in fList:
    result = foo(row, f)
    print(result)
