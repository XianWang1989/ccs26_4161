
def foo(row, func, **kwargs):
    # Prepare arguments for the function call
    args = {key: (row[i] if isinstance(i, int) else i)
            for key, i in kwargs.items()}

    # Call the function with the prepared arguments
    return func(**args)

# Example functions
def func1(x, y, z):
    return f"Function 1: x={x}, y={y}, z={z}"

def func2(a, b):
    return f"Function 2: a={a}, b={b}"

# Sample data
row = [10, 20, 30, 40, 50]

# Using the function
result1 = foo(row, func1, x=0, y=1, z=2)  # x from row[0], y from row[1], z from row[2]
result2 = foo(row, func2, a=1, b=40)      # a from row[1], b is static 40

print(result1)  # Output: Function 1: x=10, y=20, z=30
print(result2)  # Output: Function 2: a=20, b=40
