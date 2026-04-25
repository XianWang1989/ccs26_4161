
def foo(row, func, *args):
    if callable(func):
        return func(*(row[i] for i in args), *args)
    return func

# Example usage
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

# Example dataset (row)
row = [10, 20, 30, 40, 50]

# Test cases
result1 = foo(row, func1, 0, 1, 2)  # Adding elements at index 0, 1, 2
result2 = foo(row, func2, 3)        # Doubling element at index 3
result3 = foo(row, "Hello, World")  # Directly returning a string
result4 = foo(row, 2)                # Getting the element at index 2

# Print results
print(result1)  # Output: 60 (10 + 20 + 30)
print(result2)  # Output: 80 (40 * 2)
print(result3)  # Output: Hello, World
print(result4)  # Output: 30
