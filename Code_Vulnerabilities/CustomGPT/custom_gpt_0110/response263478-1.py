
def foo(row, f, *args, **kwargs):
    # If the function f is a string, return it as-is
    if isinstance(f, str):
        return f
    # If f is an int, treat it as an index for the row
    elif isinstance(f, int):
        return row[f]
    else:
        # Call the function f with dynamically constructed arguments
        # Combine elements from row with args and kwargs
        return f(*(row[i] for i in f['indices']), *args, **kwargs)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x, y, z=0):
    return x * y + z

# Usage example
row = [10, 20, 30, 40, 50]
fList = [
    {'function': func1, 'indices': [0, 1, 2]},  # Pass row[0], row[1], row[2]
    {'function': func2, 'indices': [1, 2], 'args': [5], 'kwargs': {'z': 10}},  # Pass row[1], row[2] + 10
    "Hello, World",
    2
]

# Calling foo with the fList items
for item in fList:
    result = foo(row, item['function'], *item.get('args', []), **item.get('kwargs', {}))
    print(result)
