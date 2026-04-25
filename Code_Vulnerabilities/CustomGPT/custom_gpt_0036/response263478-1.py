
from functools import partial

def foo(row, func, *args, **kwargs):
    # Extract the specific elements from the row based on the provided indices
    extracted_args = [row[i] for i in args]
    # Call the function with extracted row elements and any static arguments
    return func(*extracted_args, **kwargs)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x, y, static_param=0):
    return x * y + static_param

# Example data row
row = [10, 20, 30, 40, 50]

# Using foo with specific indices from row
result1 = foo(row, func1, 0, 1, 2)  # Passing row[0], row[1], row[2] to func1
print(result1)  # Output: 60

# Using foo with static arguments for func2
result2 = foo(row, func2, 2, 3, static_param=5)  # Passing row[2] and row[3] to func2
print(result2)  # Output: 1235 (30 * 40 + 5)
