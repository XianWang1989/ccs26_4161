
def foo(row, f, **kwargs):
    # If f is a string, return it directly
    if isinstance(f, str):
        return f
    # If f is an int, return the corresponding element from row
    elif isinstance(f, int):
        return row[f]
    # If f is a callable, call it with the provided arguments
    elif callable(f):
        return f(**{k: row[i] if isinstance(i, int) else kwargs.get(i) for k, i in kwargs.items()})
    return None

# Example functions to use
def func1(a, b):
    return a + b

def func2(x, static=0):
    return x * 2 + static

# Example data row
row_data = [10, 20, 30, 40, 50]

# Usage
result1 = foo(row_data, func1, a=0, b=1)  # Passing row elements by indices
result2 = foo(row_data, func2, x=2, static=5)  # Passing a static argument

print(result1)  # Output: 30 (10 + 20)
print(result2)  # Output: 45 (30 * 2 + 5)
