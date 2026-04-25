
def foo(row, f, *static_args):
    """
    Calls the function f with elements from row at specified indices,
    and also allows static arguments to be passed.

    :param row: List of values to extract from
    :param f: A function to be called with row elements and static args
    :param static_args: Additional static arguments to include in the call
    :return: The result of calling f with specified elements and static args
    """
    if callable(f):  # Ensure f is a callable function
        return f(*static_args)  # Call f with static arguments
    else:
        raise ValueError("The provided function is not callable.")

# Example user-defined functions
def func1(a, b):
    return a + b

def func2(x, y, z):
    return x * y + z

# Using foo with static arguments and row values
row = [10, 20, 30, 40, 50]

# Call func1 with row values at indices 0 and 1
result1 = foo(row, func1, row[0], row[1])  # 10 + 20 = 30
print(result1)  # Output: 30

# Call func2 with row values at indices 1, 3, and a static value
result2 = foo(row, func2, row[1], row[3], 5)  # 20 * 40 + 5 = 805
print(result2)  # Output: 805
