
def foo(row, *args):
    # Extract values from row based on args
    values = []
    static_args = []

    for arg in args:
        if isinstance(arg, int):
            values.append(row[arg])  # Get value from row by index
        elif isinstance(arg, str):
            static_args.append(arg)  # Collect static arguments
        else:
            raise ValueError("Arguments must be int (index) or str (static value)")

    return values, static_args

# Example functions
def func1(a, b):
    return a + b

def func2(a, b, c):
    return a * b - c

# Use the functions with the row
row = [10, 20, 30, 40]

# Call with specific indices and static values
result1 = func1(*foo(row, 0, 1))  # Passes row[0] and row[1]
result2 = func2(*foo(row, 0, 1, 'static', 2))  # Passes row[0], row[1], 'static', and row[2]

print(result1)  # Output: 30
print(result2)  # Output: 180
