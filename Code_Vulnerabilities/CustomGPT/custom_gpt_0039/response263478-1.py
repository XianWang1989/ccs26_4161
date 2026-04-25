
def foo(row, f, **kwargs):
    if callable(f):
        # Combine row elements with additional kwargs
        all_kwargs = {**{key: row[index] for key, index in kwargs.items()}, **kwargs}
        return f(**all_kwargs)
    else:
        return f

# Example functions
def func1(x, y, z):
    return x + y + z

def func2(a, b):
    return a * b

# Using foo with a specific row
row = [10, 20, 30, 40]

# Example fList
fList = [
    (func1, {'x': 0, 'y': 1, 'z': 2}),
    (func2, {'a': 2, 'b': 'index'}),  # can include predefined keys
    'Hello, World',
    2
]

# Example usage
for f in fList:
    if isinstance(f, tuple):
        func, indices = f
        result = foo(row, func, **indices)
    else:
        result = foo(row, f)

    print(result)
