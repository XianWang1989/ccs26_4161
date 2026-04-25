
# Sample functions
def func1(x, y, z):
    return x + y + z

def func2(a, b):
    return a * b

# Main function where users can specify row elements and static arguments
def foo(row, f, *args, **kwargs):
    # Gather specified elements from the row based on their indices
    row_args = [row[i] for i in f]  # `f` contains indices of row elements
    # Call the function with row_args, static args and any keyword args
    return f(*row_args, *args, **kwargs)

# Example usage
row = [10, 20, 30, 40, 50]  # Sample data row

# Calling func1 with elements from row at indices 0, 1, and passing an additional static argument
result1 = foo(row, func1, [0, 1])  # Uses row[0] and row[1] for the call
print(result1)  # Output: 60 (10 + 20 + 30 from row)

# Calling func2 with elements from row at indices 3, and an additional static argument
result2 = foo(row, func2, [3, 2])  # Uses row[3] (40) and static element 2
print(result2)  # Output: 80 (40 * 2)

# Example with another function with keyword arguments
def func3(a, b, c=1):
    return a + b + c

result3 = foo(row, func3, [2, 4], c=3)  # Uses row[2] (30), row[4] (50) and the static c=3
print(result3)  # Output: 83 (30 + 50 + 3)
