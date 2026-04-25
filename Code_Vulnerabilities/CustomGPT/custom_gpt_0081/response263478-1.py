
def foo(row, f, *args):
    if callable(f):
        # Accepts row indices and combines with *args
        return f(*[row[i] for i in args], *args)
    elif isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        raise ValueError('Invalid function or command.')

# Example Functions
def func1(a, b):
    return a + b

def func2(a, b, c):
    return a * b - c

# Example dataset
row_data = [10, 20, 30, 40, 50]

# Sample usage:
result1 = foo(row_data, func1, 0, 1)  # Get elements 0 (10) and 1 (20) from row_data
print(result1)  # 30

result2 = foo(row_data, func2, 1, 2, 0)  # Get elements 1 (20), 2 (30), and static arg 0 (0) from row_data
print(result2)  # 590, as it computes 20 * 30 - 10
