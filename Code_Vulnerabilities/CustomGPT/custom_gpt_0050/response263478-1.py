
def foo(row, func, *args):
    # Collect arguments to pass to the function
    final_args = []

    # Retrieve arguments from the row
    for arg in args:
        if isinstance(arg, int) and 0 <= arg < len(row):
            final_args.append(row[arg])
        else:
            final_args.append(arg)  # static arguments

    return func(*final_args)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(a):
    return a * 2

# Example row
row = [10, 20, 30, 40, 50]

# Using the foo function
result1 = foo(row, func1, 0, 1, 4)  # passes row[0], row[1], and 50
result2 = foo(row, func2, 2)        # passes row[2]

print(result1)  # Output: 80 (10 + 20 + 50)
print(result2)  # Output: 60 (30 * 2)
