
def foo(row, func, *args):
    # Extract the specific elements from `row` based on the provided indices
    row_args = [row[i] for i in range(len(row)) if i in args]
    return func(*row_args)

# Example functions
def func1(a, b):
    return a + b

def func2(a, b, c):
    return a * b + c

# Example usage
row = [10, 20, 30, 40]

# Pass specific indices from `row` and additional static arguments
result1 = foo(row, func1, 0, 1)  # Passes row[0] and row[1] to `func1`
result2 = foo(row, func2, 0, 1, 2)  # Passes row[0], row[1], and an additional static argument

print(result1)  # Output: 30
print(result2)  # Output: 230
