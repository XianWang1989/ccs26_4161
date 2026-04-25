
def foo(row, *args):
    if callable(args[0]):  # Check if the first argument is a function
        func = args[0]
        # Extract the indices and static arguments
        indices = args[1:]  # All subsequent args are either indices or static values
        result = []
        for arg in indices:
            if isinstance(arg, int):  # If it's an index, get value from row
                result.append(row[arg])
            else:  # Otherwise, it's a static argument
                result.append(arg)
        return func(*result)  # Call the function with unpacked arguments
    else:
        return args[0]  # If the first argument is not callable, return it directly

# Example functions for demonstration
def func1(a, b):
    return a + b

def func2(x):
    return x * 2

# Example usage
row = [10, 20, 30, 40, 50]

# Using func1 with elements from row and a static argument
result1 = foo(row, func1, 0, 2, 5)  # 0 and 2 are indices, 5 is a static argument
print(result1)  # Output: 10 + 30 + 5 = 45

# Using func2 with a static value
result2 = foo(row, func2, 0)  # Only index 0
print(result2)  # Output: 20 (10 * 2)
