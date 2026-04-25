
def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    elif callable(f):
        return f()  # Call the function if no arguments are provided
    elif isinstance(f, dict):
        func = f.get('function')
        args = f.get('args', [])
        return func(*[row[i] if isinstance(i, int) else i for i in args])

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

def static_value():
    return "Static Value"

# Example usage
fList = [
    {'function': func1, 'args': [1, 0, 4]},  # Using indices
    {'function': func2, 'args': [5]},         # Pass an index and static argument
    'Hello, World',
    2,
    static_value                             # No args
]

row = [10, 20, 30, 40, 50]

# Test the foo function with different elements of fList
results = [foo(row, f) for f in fList]

print(results)  # Output from the specified elements
