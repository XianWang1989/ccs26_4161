
def foo(row, func, *args):
    # Extract specified elements from the row using the indices
    elements = [row[i] for i in args if isinstance(i, int)]
    # Call the function with the extracted elements and any additional arguments
    return func(*elements)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x, y):
    return x * y

# Using the function
row = [10, 20, 30, 40, 50]

# Specifying indices 0, 2 (from the row) and static argument 5 for func1
result1 = foo(row, func1, 0, 2, 5)  # 10 + 30 + 5 = 45
print(result1)

# Specifying indices 1, 3 for func2
result2 = foo(row, func2, 1, 3)  # 20 * 40 = 800
print(result2)
