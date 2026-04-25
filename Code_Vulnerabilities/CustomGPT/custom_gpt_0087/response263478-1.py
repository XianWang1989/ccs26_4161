
def foo(row, f, *args):
    # If f is a string, return it directly
    if isinstance(f, str):
        return f
    # If f is an int, return the corresponding element from row
    elif isinstance(f, int):
        return row[f]
    # If f is callable, get the necessary row elements and static arguments
    elif callable(f):
        return f(*args)

# Example functions
def func1(x, y):
    return x + y

def func2(a, b, c):
    return a * b + c

# Example usage
row = [1, 2, 3, 4, 5]

# Specifying which elements to pass with static arguments
result1 = foo(row, func1, row[0], row[2])  # 1 and 3
result2 = foo(row, func2, 1, 2, 3)          # static arguments

print(result1)  # Output: 4
print(result2)  # Output: 5
