
def foo(row, func, *args, **kwargs):
    # Extract values from row based on the provided keys
    args_from_row = [row[i] for i in args]

    # Combine row values with static arguments
    all_args = args_from_row + list(kwargs.values())

    return func(*all_args)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x, static_val):
    return x * static_val

# Example usage
row = [10, 20, 30, 40]
fList = [
    (func1, 0, 1, 2),                      # Pass row[0], row[1], row[2]
    (func2, 3),                            # Pass row[3] and a static value
]

# Invoke functions
for function, *args in fList:
    result = foo(row, function, *args, static_val=2)
    print(result)
