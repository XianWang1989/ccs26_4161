
def foo(row, f, **kwargs):
    if callable(f):
        args = [row[i] for i in kwargs.get('row_indices', [])]
        static_args = kwargs.get('static', [])
        return f(*args, *static_args)
    else:
        return f

# Example functions
def func1(a, b):
    return a + b

def func2(x, y, c):
    return x * y + c

# Define fList
fList = [
    (func1, {'row_indices': [1, 0], 'static': []}),  # func1(row[1], row[0])
    (func2, {'row_indices': [0, 2], 'static': [5]}), # func2(row[0], row[2], 5)
    'Hello, World',
    3
]

# Example row
row = [10, 20, 30]

# Testing the foo function
for item in fList:
    result = foo(row, *item) if isinstance(item, tuple) else foo(row, item)
    print(result)
