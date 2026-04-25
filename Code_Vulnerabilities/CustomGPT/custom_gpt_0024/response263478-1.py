
def foo(row, f, *args, **kwargs):
    if callable(f):
        # Call the function with specified row elements and additional arguments
        return f(*args, **kwargs)
    elif isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        raise ValueError("Unsupported function type.")

# Example functions
def func1(a, b):
    return a + b

def func2(a, b, c):
    return a * b + c

# Example row
row = [10, 20, 30, 40, 50]

# Using foo with static elements and row elements
result1 = foo(row, func1, row[1], row[3])  # Uses elements 20 and 40
result2 = foo(row, func2, row[0], row[2], 5)  # Uses elements 10, 30, and static 5

print(result1)  # Output: 60 (20 + 40)
print(result2)  # Output: 305 (10 * 30 + 5)
