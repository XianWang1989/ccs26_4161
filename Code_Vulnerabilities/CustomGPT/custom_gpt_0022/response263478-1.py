
def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    elif callable(f):
        return f()
    elif isinstance(f, tuple):
        func, *args = f
        resolved_args = [foo(row, arg) for arg in args]
        return func(*resolved_args)
    else:
        raise ValueError("Unsupported value type in f")

# Define some sample functions
def func1(a, b):
    return a + b

def func2(x):
    return x * 2

def func3(s):
    return s.upper()

# Example row
row = [10, 20, 30, 40, 50]

# Function list with mixed element types
fList = [
    (func1, 0, 1),          # Pass elements at index 0 and 1 from row
    (func2, 2),            # Pass element at index 2 from row
    (func3, 'hello'),      # Static argument
    'Hello, World',        # String
    2                      # Index from row
]

# Testing the foo function with different elements from fList
for f in fList:
    print(foo(row, f))
