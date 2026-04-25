
def foo(row, f):
    if isinstance(f, str):
        return f  # If it's a string, return it directly
    elif isinstance(f, int):
        return row[f]  # If it's an int, return the specific row element
    else:
        # It should be a tuple (function, indices)
        func, indices = f
        args = [row[i] for i in indices]  # Extract row elements based on indices
        return func(*args)  # Call the function with those elements

# Example functions
def func1(x, y, z):
    return x + y - z

def func2(a, b, c):
    return a * b + c

# Example list of functions and indices
fList = [
    (func1, [1, 0, 4]),  # Calls func1 with row[1], row[0], row[4]
    (func2, [0, 2, 3]),  # Calls func2 with row[0], row[2], row[3]
    'Hello, World',
    2
]

# Example row
row = [10, 20, 30, 40, 50]

# Usage
for f in fList:
    result = foo(row, f)
    print(result)
