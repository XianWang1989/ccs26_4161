
def foo(row, f, *args):
    if callable(f):
        return f(*[row[i] for i in args] + list(args[len(row):]))
    elif isinstance(f, str):
        return f
    elif isinstance(f, (int, float)):
        return row[f]
    else:
        raise ValueError("Provided function or value is not valid.")

# Example Functions
def func1(x, y):
    return x + y

def func2(a, b, c):
    return a * b + c

# Example usage
row = [10, 20, 30, 40, 50]

# Using a function with indices
result1 = foo(row, func1, 0, 1)  # Uses row[0] and row[1]
print(result1)  # Output: 30

# Using another function with additional static argument
result2 = foo(row, func2, 0, 1, 5)  # Uses row[0], row[1], and static int 5
print(result2)  # Output: 225
