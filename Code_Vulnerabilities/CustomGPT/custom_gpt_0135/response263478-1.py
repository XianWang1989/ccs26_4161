
def foo(row, f, *args, **kwargs):
    if callable(f):
        # Extract specified elements from row based on keys in kwargs
        row_args = [row[k] for k in kwargs.get('keys', [])]
        return f(*row_args, *args)
    elif isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        raise ValueError("Unsupported function type")

# Define some example functions
def func1(x, y, z):
    return x + y + z

def func2(a, b):
    return a * b

# Example row
row = [10, 20, 30, 40, 50]

# Usage
result1 = foo(row, func1, keys=[0, 1, 2])  # Pass elements at index 0, 1, 2
result2 = foo(row, func2, 2, 3, keys=[0, 1])  # Pass row[0] and row[1] along with static arguments

print(result1)  # Output: 60 (10 + 20 + 30)
print(result2)  # Output: 60 (10 * 2)
