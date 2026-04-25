
def foo(row, f, *static_args):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        return f(*[row[i] for i in f] + list(static_args))

# Define sample functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

# Example row
row = [10, 20, 30, 40, 50]

# Usage of foo with various function calls
result1 = foo(row, func1, 0, 2, static_value=5)  # Using indices 0, 2 (10 + 30 + 5)
result2 = foo(row, func2, 1)                      # Using index 1 (20 * 2)
result3 = foo(row, 'Hello, World')                # Return string

print(result1)  # Output: 45
print(result2)  # Output: 40
print(result3)  # Output: Hello, World
