
def foo(row, f, *args):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        return f(*args)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

def func3(str1, str2):
    return f"{str1} and {str2}"

# Example row
row = [10, 20, 30, 40, 50]

# Example function list
fList = [
    (func1, row[1], row[0], 5),  # Using elements from row with a static argument
    (func2, row[2]),             # Using an element from row
    (func3, 'spam', 'eggs'),     # Static arguments
    'Hello, World',
    2                          # Directly returns element at index 2 from row
]

# Testing the foo function
for f in fList:
    result = foo(row, *f) if isinstance(f, tuple) else foo(row, f)
    print(result)
