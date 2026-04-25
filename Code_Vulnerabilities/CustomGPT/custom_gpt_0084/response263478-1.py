
def foo(row, f, **kwargs):
    """Calls a function f with row elements and additional static arguments."""
    if callable(f):
        return f(*(row[i] for i in kwargs.get('indices', [])), *kwargs.get('static', []))
    elif isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        raise ValueError("Unsupported function type")

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

# Usage
row = [10, 20, 30, 40, 50]
fList = [
    (func1, {'indices': [0, 1, 2], 'static': []}),
    (func2, {'indices': [3], 'static': []}),
    'Hello, World',
    2
]

# Calling foo for different elements
for item in fList:
    if isinstance(item, tuple):
        func, params = item
        result = foo(row, func, **params)
        print(result)
    else:
        print(foo(row, item))
