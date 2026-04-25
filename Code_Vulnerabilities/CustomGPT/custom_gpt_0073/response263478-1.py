
def foo(row, f, *args, **kwargs):
    # Extract specified elements from row using the indices in args
    row_args = [row[i] for i in args]
    # Call the function with both row arguments and static kwargs
    return f(*row_args, **kwargs)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x, y=10):
    return x * y

# Usage
row = [1, 2, 3, 4, 5]

# Calling func1 with specific elements from row and a static argument
result1 = foo(row, func1, 0, 1, 2)  # Uses row[0], row[1], row[2]
print(result1)  # Output: 6 (1 + 2 + 3)

# Calling func2 with specific elements and a keyword argument
result2 = foo(row, func2, 0, y=5)  # Uses row[0] and sets y=5
print(result2)  # Output: 5 (1 * 5)
