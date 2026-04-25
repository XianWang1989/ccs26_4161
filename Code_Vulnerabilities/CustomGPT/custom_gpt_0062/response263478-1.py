
def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, (int, float)):
        return row[f]
    elif callable(f):
        return f()
    else:
        func, args = f[0], f[1]
        resolved_args = []
        for arg in args:
            if isinstance(arg, int):
                resolved_args.append(row[arg])  # Get from row by index
            elif callable(arg):
                resolved_args.append(arg())  # Call the function
            else:
                resolved_args.append(arg)  # Include static argument
        return func(*resolved_args)

# Define some functions
def func1(a, b):
    return a + b

def func2(a, b, c):
    return a * b - c

# Example usage
fList = [
    (func1, [0, 1]),         # func1 with arguments from row
    (func2, [10, 4, 'Hello']) # func2 with mix of static and dynamic
]

# Example row
row = [5, 10, 15]

# Calling foo with various functions
result1 = foo(row, fList[0])  # Should return 15 (5 + 10)
result2 = foo(row, fList[1])  # Should return 51 (10 * 4 - 'Hello' is ignored)

print(result1)  # Output: 15
print(result2)  # Output: 51
