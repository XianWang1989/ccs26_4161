
def foo(row, f, *args, **kwargs):
    # Prepare arguments: elements from row based on keyword arguments and additional args
    row_args = [row[i] for i in kwargs.get('indices', [])]
    return f(*row_args, *args)

# Example functions
def func1(x, y, z):
    return x + y + z

def func2(a, b):
    return a * 2 + b

# Example usage
row_data = [1, 2, 3, 4, 5]

# Calling func1 with indices 0, 1, and additional argument 10
result1 = foo(row_data, func1, 10, indices=[0, 1])  # 1 + 2 + 10 = 13

# Calling func2 with indices 3 and 4
result2 = foo(row_data, func2, indices=[3, 4])  # 4 * 2 + 5 = 13

print(result1)  # Output: 13
print(result2)  # Output: 13
