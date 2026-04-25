
def foo(row, func, *args):
    # Extract arguments based on their types
    kwargs = {}
    for arg in args:
        if isinstance(arg, str):
            kwargs[arg] = row[arg]
        elif isinstance(arg, int):
            kwargs[f'arg{arg}'] = row[arg]
        else:
            kwargs[f'arg{arg}'] = arg

    return func(**kwargs)

# Example functions
def func1(arg1, arg0, static=0):
    return arg1 + arg0 + static

def func2(arg0):
    return f"Hello, {arg0}"

# Sample data row
row = [10, 20, 30, 40, 50]

# Using the function
result1 = foo(row, func1, 1, 0, static=5)  # row[1] + row[0] + 5
print(result1)  # Outputs: 35

result2 = foo(row, func2, 0)  # row[0]
print(result2)  # Outputs: Hello, 10
