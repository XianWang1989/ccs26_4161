
def foo(row, f, *args, **kwargs):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        # Extract the row elements based on the user-defined arguments
        func_args = [row[i] for i in args if i < len(row)]
        # Call the function with both the chosen row elements and extra kwargs
        return f(*func_args, **kwargs)

# Example functions
def func1(a, b, c, static_arg=None):
    return a + b + c + (static_arg if static_arg is not None else 0)

row = [10, 20, 30, 40, 50]

# Calling foo
result = foo(row, func1, 0, 1, 2, static_arg=100)
print(result)  # Output: 170
