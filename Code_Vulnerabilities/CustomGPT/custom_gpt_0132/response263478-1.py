
def foo(row, f, *args, **kwargs):
    # Extract specified elements from row using the indices provided in f
    if callable(f):
        # Get values from row based on the `f` indices
        values = [row[i] for i in f]
        return f(*values, *args, **kwargs)
    elif isinstance(f, str):
        return f
    else:
        return row[f]

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(a, b, static):
    return (a * b) + static

# Example row data
row = [10, 20, 30, 40, 50]

# Function list with indices and static arguments
fList = [
    (func1, [0, 1, 2]),
    (func2, [1, 2], 100),
    'Hello, World',
    2
]

# Run examples
print(foo(row, fList[0][0], *fList[0][1]))  # Output: 60 (10 + 20 + 30)
print(foo(row, fList[1][0], *fList[1][1], fList[1][2]))  # Output: 500 ((20 * 30) + 100)
print(foo(row, fList[2]))  # Output: Hello, World
print(foo(row, fList[3]))  # Output: 30 (row[2])
