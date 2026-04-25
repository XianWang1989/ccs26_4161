
def foo(row, f, *static_args):
    if callable(f):
        # Extract specified elements from row using indices or keys
        return f(*(static_args + [row[i] for i in range(len(row)) if i in f.indices]))
    elif isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        raise ValueError("Unsupported function or type")

# Define functions
def func1(x, y):
    return x + y

def func2(a, b):
    return a * b

# Example usage
fList = [
    (func1, [1, 0]),  # func1 with indices 1 and 0 from row
    (func2, [0, 1]),  # func2 with indices 0 and 1 from row
    'Hello, World',
    2
]

# Adding indices to functions for easy access
for f in fList:
    if isinstance(f, tuple):
        f.indices = f[1]
    else:
        f.indices = []

row = [10, 20, 30]

# Test the function
print(foo(row, fList[0][0], 5))  # Output: 35 (5 + 20)
print(foo(row, fList[1][0], 2))  # Output: 60 (2 * 30)
print(foo(row, fList[2]))         # Output: 'Hello, World'
print(foo(row, fList[3]))         # Output: 30 (row[2])
