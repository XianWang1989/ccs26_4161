
def foo(row, func, *args):
    """Calls the specified function with elements from row and additional static arguments."""
    # Prepare the arguments, binding row elements with the specified indices
    bound_args = [row[i] if isinstance(i, int) else i for i in args]

    # Call the function with the prepared arguments
    return func(*bound_args)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

# Usage
row = [10, 20, 30, 40]

# Define function calls
result1 = foo(row, func1, 0, 1, 2)  # Passes row[0], row[1], row[2]
result2 = foo(row, func2, 3)        # Passes row[3]

print(result1)  # Output: 60 (10 + 20 + 30)
print(result2)  # Output: 80 (40 * 2)
