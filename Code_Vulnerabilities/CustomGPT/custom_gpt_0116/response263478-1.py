
from functools import partial

def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        # Use partial to allow static arguments alongside row elements
        return f['func'](*[row[i] for i in f['args']] + f.get('static_args', []))

# Example functions
def func1(x, y, z):
    return x + y + z

def func2(a, b, c):
    return a * b - c

# Example usage
row = [10, 20, 30, 40, 50]
fList = [
    {'func': func1, 'args': [0, 1, 2]},
    {'func': func2, 'args': [0, 1], 'static_args': [5]},
    'Hello, World',
    2
]

# Outputs
for f in fList:
    print(foo(row, f))
