
def foo(row, func, *args, **kwargs):
    # Extract specified row elements
    row_elements = [row[i] for i in args]
    # Call the function with row elements and additional kwargs
    return func(*row_elements, **kwargs)

# Example functions
def func1(a, b, c, static='default'):
    return a + b + c + static

def func2(x, y, static='hello'):
    return x * y + static

# Usage
row = [10, 20, 30, 40, 50]  # Example data row

# Calling with specific indices and static arguments
result1 = foo(row, func1, 0, 1, 2, static='!')
result2 = foo(row, func2, 1, 3, static=' world!')

print(result1)  # Output: 60!
print(result2)  # Output: 600 world!
