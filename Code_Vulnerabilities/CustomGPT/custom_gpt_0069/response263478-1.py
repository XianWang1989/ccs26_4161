
def foo(row, f, *args, **kwargs):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    elif callable(f):
        return f(*(row[i] for i in kwargs.get('indices', [])), *args, **kwargs)
    else:
        raise ValueError("Invalid function or type provided.")

# Example functions
def func1(x, y, z):
    return x + y + z

def func2(a, b):
    return a * b

# Example row
row = [10, 20, 30, 40, 50]

# Example function calls
result1 = foo(row, func1, indices=[0, 1, 2])  # Pass elements 0, 1, and 2 from row to func1
result2 = foo(row, func2, 2, indices=[2, 3])  # Pass elements 2 and 3 to func2, with an additional arg

print(result1)  # Output: 60
print(result2)  # Output: 120
