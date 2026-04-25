
def foo(row, f, **kwargs):
    if callable(f):
        # Extract arguments from row and kwargs
        args = [row[i] for i in kwargs.get('row_indices', [])]
        return f(*args, **{k: v for k, v in kwargs.items() if k != 'row_indices'})
    else:
        return f  # Return any other non-callable directly

# Example functions
def func1(a, b, c):
    return a + b * c

def func2(x):
    return x * 2

# Example usage
row = [10, 20, 30, 40, 50]
result1 = foo(row, func1, row_indices=[0, 1, 2])  # Uses row[0], row[1], row[2]
result2 = foo(row, func2, row_indices=[3])  # Uses row[3]
static_result = foo(row, "Hello, World")  # Static string

print(result1)  # Output from func1
print(result2)  # Output from func2
print(static_result)  # Output: Hello, World
