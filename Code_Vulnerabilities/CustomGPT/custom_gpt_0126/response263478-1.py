
def foo(row, selector):
    if isinstance(selector, str):
        return selector
    elif isinstance(selector, int):
        return row[selector]
    elif callable(selector):
        return selector(*row)  # Assuming row directly holds the required args
    else:
        func, args = selector
        return func(*(row[i] for i in args))  # Extract elements from row based on args

# Example functions
def func1(x, y, z):
    return x + y + z

def func2(a, b):
    return a * b

# Example dataset
row = [10, 20, 30, 40, 50]

# Example function list
fList = [
    (func1, [0, 1, 2]),  # Uses row[0], row[1], row[2]
    (func2, [1, 3]),     # Uses row[1] and row[3]
    'Hello, World',
    2
]

# Test the foo function
for f in fList:
    result = foo(row, f)
    print(result)
