
def foo(row, f, **kwargs):
    if callable(f):
        return f(*[row[i] for i in kwargs.get('indices', [])], **kwargs)
    elif isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        raise ValueError("Function must be callable, a string, or an integer.")

# Example functions to use
def func1(a, b):
    return a + b

def func2(x, static_arg):
    return x * static_arg

# Example usage
fList = [
    (func1, {'indices': [1, 0]}),  # uses elements at row[1] and row[0]
    (func2, {'indices': [2], 'static_arg': 10}),  # uses row[2] and static argument
    'Hello, World',
    2
]

# Sample row
row = [5, 3, 2]

for f in fList:
    if isinstance(f, tuple):
        result = foo(row, f[0], **f[1])
    else:
        result = foo(row, f)
    print(result)
