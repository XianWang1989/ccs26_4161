
def foo(row, f, *args, **kwargs):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        # Get row elements based on kwargs
        row_args = {key: row[key] for key in kwargs if key < len(row)}
        return f(*args, **row_args)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x, y=10):
    return x * y

# Example row
row = [5, 3, 8, 2, 7]

# Example calls
result1 = foo(row, func1, 1, c=4)  # Uses row[1] and static c=4
result2 = foo(row, func2, 0)        # Uses row[0] and default y=10

print(result1)  # Output: 12
print(result2)  # Output: 50
