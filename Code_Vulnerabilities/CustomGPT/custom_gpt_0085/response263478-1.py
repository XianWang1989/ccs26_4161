
def foo(row, f):
    # If f is a string, return it directly
    if isinstance(f, str):
        return f
    # If f is an integer, return the row element at that index
    elif isinstance(f, int):
        return row[f]
    # If f is a callable function
    elif callable(f):
        return f()
    # If f is a tuple, unpack arguments
    elif isinstance(f, tuple):
        func, args = f
        return func(*[foo(row, arg) if isinstance(arg, (int, str)) else arg for arg in args])

# Sample function definitions
def func1(a, b, static_value):
    return a + b + static_value

def func2(x):
    return x * 2

def func3(a, b):
    return a + " " + b

# Example usage
row_data = [10, 20, 30, 40]  # Example row data
fList = [
    (func1, [1, 0, 100]),      # Adds row[1] + row[0] + 100
    (func2, [3]),              # Multiplies static value from row[3] by 2
    (func3, ['Hello', 'World']) # Concatenates 'Hello' and 'World'
]

# Test the function
for f in fList:
    result = foo(row_data, f) if isinstance(f, tuple) else foo(row_data, f)
    print(result)
