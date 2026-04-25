
def foo(row, f, **kwargs):
    if callable(f):
        # Gather arguments based on keys from kwargs
        args = [row[k] for k in kwargs.get('row_keys', [])]
        # Include additional static arguments
        return f(*args, **{k: v for k, v in kwargs.items() if k != 'row_keys'})
    elif isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        raise ValueError("Unsupported function type")

# Example functions
def func1(a, b, static_arg=None):
    return a + b + (static_arg if static_arg else 0)

def func2(x):
    return x ** 2

# Example row
row = [10, 20, 30, 40, 50]

# Using the enhanced foo function
result1 = foo(row, func1, row_keys=[0, 1], static_arg=5)  # 10 + 20 + 5 = 35
result2 = foo(row, func2, row_keys=[2])  # 30 ** 2 = 900

print(result1)  # Output: 35
print(result2)  # Output: 900
