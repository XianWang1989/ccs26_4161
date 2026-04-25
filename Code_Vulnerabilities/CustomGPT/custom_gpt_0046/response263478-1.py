
def foo(row, func, *args, **kwargs):
    # Gather values from the row based on provided indices
    row_args = [row[i] for i in args if isinstance(i, int)]
    # Call the function with all arguments
    return func(*row_args, **kwargs)

# Example functions
def func1(a, b, static=0):
    return a + b + static

def func2(a, b, c):
    return a * b - c

# Example row (like a record from a dataset)
row = [10, 20, 30, 40]

# Usage examples
result1 = foo(row, func1, 0, 1, static=5)  # Pass indices 0 and 1, static argument
result2 = foo(row, func2, 1, 2, c=5)       # Pass indices 1 and 2, with c as a keyword argument

print(result1)  # Output: 35 (10 + 20 + 5)
print(result2)  # Output: 15 (20 * 30 - 5)
