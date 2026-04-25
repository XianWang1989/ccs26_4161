
def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    elif isinstance(f, dict):
        func = f['func']
        args = [
            row[i] for i in f.get('row_indices', [])
        ] + f.get('static_args', [])
        return func(*args)
    else:
        raise ValueError("Invalid input format")

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x, y):
    return x * y

# Example row of data
row = [10, 20, 30, 40, 50]

# Example function list
fList = [
    {'func': func1, 'row_indices': [0, 1, 2], 'static_args': []},
    {'func': func2, 'row_indices': [3], 'static_args': [5]},
    'Hello, World',
    2
]

# Using foo to call functions
for f in fList:
    result = foo(row, f)
    print(result)
