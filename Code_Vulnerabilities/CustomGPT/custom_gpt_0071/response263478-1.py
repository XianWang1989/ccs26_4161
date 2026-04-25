
def foo(row, f):
    if callable(f):
        return f(*row)  # Directly call the function with all elements of row
    elif isinstance(f, dict):
        func = f['func']
        args = [row[i] if i in f['indices'] else f['static'][i] for i in range(len(f['static']))]
        return func(*args)
    return f  # Handle string or other types directly

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

# Define function list
fList = [
    {'func': func1, 'indices': [1, 0], 'static': [5]},
    {'func': func2, 'indices': [4], 'static': []},
    'Hello, World',
    2
]

# Sample row
row = [10, 20, 30, 40, 50]

# Testing foo
for f in fList:
    result = foo(row, f)
    print(result)
