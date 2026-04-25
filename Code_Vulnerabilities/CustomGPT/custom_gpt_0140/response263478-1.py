
def foo(row, func, *args, **kwargs):
    # Prepare the arguments for the function
    # Use args for static arguments and kwargs for row indices
    resolved_args = [row[index] for index in args]
    resolved_kwargs = {key: row[value] for key, value in kwargs.items()}

    # Combine all arguments
    return func(*resolved_args, **resolved_kwargs)

# Example functions
def func1(a, b):
    return a + b

def func2(x, y=0):
    return x * 2 + y

# Example row
row = [10, 20, 30, 40, 50]

# Call foo with specific indices and static arguments
result1 = foo(row, func1, 1, 0)  # Pass row[1] and row[0] to func1
result2 = foo(row, func2, 2, y=5)  # Pass row[2] and a static argument y=5 to func2

print(result1)  # Output: 30
print(result2)  # Output: 65
