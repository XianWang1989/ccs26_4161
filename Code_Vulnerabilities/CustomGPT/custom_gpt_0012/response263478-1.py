
def foo(row, func, *args, **kwargs):
    # Combine row elements with static arguments
    args = [row[i] for i in args] + list(kwargs.values())
    return func(*args)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(a, b, static_arg):
    return a * b + static_arg

# Example usage
row = [1, 2, 3, 4, 5]

# Using func1 and passing specific indices from row
result1 = foo(row, func1, 0, 2, c=4)  # This will use row[0], row[2] and static arg 4
print(result1)  # Output: 7 (1 + 3 + 4)

# Using func2 with different arguments
result2 = foo(row, func2, 1, 3, static_arg=10)  # This uses row[1], row[3] and the static arg 10
print(result2)  # Output: 16 (2 * 4 + 10)
