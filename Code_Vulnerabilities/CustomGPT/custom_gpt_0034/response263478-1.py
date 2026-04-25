
def foo(row, func, *args):
    # Construct the arguments to pass to the function
    func_args = [row[i] for i in args if isinstance(i, int)] + list(args)
    return func(*func_args)

# Sample functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

# Example usage
row = [5, 10, 15, 20]

# Calling with dynamic element indices from row
result1 = foo(row, func1, 0, 1, 2)  # Should use row[0], row[1], and row[2]
print(result1)  # Output: 30

# Calling with a static argument
result2 = foo(row, func2, 3)  # Should use row[3]
print(result2)  # Output: 40

# Calling with mixed arguments
result3 = foo(row, func1, 0, 1, 2, 100)  # Include static argument 100
print(result3)  # Output: 130
