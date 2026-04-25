
def foo(row, f, *args, **kwargs):
    # Prepare the arguments based on row data and additional static arguments
    args = [row[i] for i in args]  # Get row elements by index
    return f(*args, **kwargs)  # Call the function with collected arguments

# Example functions
def func1(a, b, c=0):
    return a + b + c

def func2(x, y):
    return x * y

# Usage example
row = [10, 20, 30, 40]

# Call func1 with elements from row and a static argument
result1 = foo(row, func1, 0, 1, c=5)  # Equivalent to func1(10, 20, c=5)
print(result1)  # Output: 35

# Call func2 with elements from row using specified indices
result2 = foo(row, func2, 2, 1)  # Equivalent to func2(30, 20)
print(result2)  # Output: 600
