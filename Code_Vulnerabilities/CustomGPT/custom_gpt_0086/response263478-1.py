
def foo(row, f, **kwargs):
    # Handle string case
    if isinstance(f, str):
        return f
    # Handle integer index case
    elif isinstance(f, int):
        return row[f]
    # Handle function case
    else:
        # Extract the required elements from row based on the indices provided
        args = [row[i] for i in f['args']]
        # Combine with any additional keyword arguments
        return f['func'](*args, **kwargs)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

# Example usage
fList = [
    {'func': func1, 'args': [1, 0, 4]},
    {'func': func2, 'args': [0]},
    'Hello, World',
    2
]

# Sample row
row = [10, 20, 30, 40, 50]

for f in fList:
    result = foo(row, f)
    print(result)
