
def foo(row, func, *static_args, **kwargs):
    # Create a tuple of arguments from the row and any additional static arguments
    args = [row[i] for i in kwargs.get('indices', [])] + list(static_args)
    return func(*args)

# Example functions
def func1(x, y, z):
    return x + y + z

def func2(a, b):
    return a * b

# Usage
row = [10, 20, 30, 40]

# Specify the indices of row elements you want to use
result1 = foo(row, func1, 5, indices=[0, 1, 2])  # 10 + 20 + 30 + 5
result2 = foo(row, func2, indices=[0, 3])        # 10 * 40

print(result1)  # Output: 65
print(result2)  # Output: 400
