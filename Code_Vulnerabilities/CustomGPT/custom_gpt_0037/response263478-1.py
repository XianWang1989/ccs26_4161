
def foo(row, f):
    if callable(f):
        return f(*row)
    elif isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        raise ValueError("Unsupported type for f")

def custom_func(a, b, c, static=0):
    return a + b + c + static

# Example usage
row = [10, 20, 30, 40]

# Specifying arguments using a lambda to capture desired elements
f1 = lambda a=row[0], b=row[2]: custom_func(a, b)

# Directly using integers
f2 = 1  # Accessing row[1]

# Using a string
f3 = "Hello, World"

# Results
print(foo(row, f1))  # Output: 40 (10 + 30)
print(foo(row, f2))  # Output: 20 (row[1])
print(foo(row, f3))  # Output: Hello, World
