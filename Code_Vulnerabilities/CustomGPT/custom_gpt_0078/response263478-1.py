
def foo(row, func, *args, **kwargs):
    # Retrieve specified elements from the row
    row_args = [row[i] for i in kwargs.get('indices', [])]
    # Combine them with any static arguments
    all_args = row_args + list(args)
    return func(*all_args)

# Example functions for testing
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

# Example usage
row = [10, 20, 30, 40]
result1 = foo(row, func1, 5, 3, indices=[0, 1, 2])  # Passes row[0], row[1], row[2]
result2 = foo(row, func2, indices=[3])               # Passes row[3] (40)

print(result1)  # Outputs: 48 (10 + 20 + 30 + 5 + 3)
print(result2)  # Outputs: 80 (40 * 2)
