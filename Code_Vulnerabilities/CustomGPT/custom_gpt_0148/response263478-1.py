
def foo(row, f, *args, **kwargs):
    if callable(f):
        # Generate the arguments to pass to the function
        function_args = [row[i] for i in args] + list(kwargs.values())
        return f(*function_args)
    else:
        return f

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

# Example data row
row = [10, 20, 30, 40, 50]

# Usage
result1 = foo(row, func1, 0, 1, c=2)  # Uses row[0], row[1], and c=2
result2 = foo(row, func2, 3)          # Uses row[3]

print(result1)  # Output: 32 (10 + 20 + 2)
print(result2)  # Output: 80 (40 * 2)
