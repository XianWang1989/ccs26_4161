
def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    elif callable(f):
        return f(row)
    elif isinstance(f, dict):
        func = f.get('func')
        args = f.get('args', [])
        return func(*[row[i] if isinstance(i, int) else i for i in args])

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

# Example dataset (row)
row = [1, 2, 3, 4]

# Function list with a more elegant structure
fList = [
    {'func': func1, 'args': [0, 1, 2]},   # Call func1 with row[0], row[1], row[2]
    {'func': func2, 'args': [0]},          # Call func2 with row[0]
    'Hello, World',                        # Static string
    1,                                     # Access row[1]
    {'func': func2, 'args': [5]},         # Call func2 with static integer 5
]

# Test the implementation
for f in fList:
    result = foo(row, f)
    print(result)
