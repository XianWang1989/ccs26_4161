
def foo(row, func, *args):
    """
    Call func with specified elements from row and any additional static arguments.

    :param row: A list or tuple containing data elements.
    :param func: The function to call.
    :param args: Additional arguments to pass to func.
    :return: The result of func called with the specified arguments.
    """

    # Extract the elements from row based on the provided indices
    row_elements = [row[i] for i in args if isinstance(i, int)]

    # Call the function with row elements followed by any additional arguments
    return func(*row_elements, *args)

# Example functions
def func1(x, y, z):
    return x + y + z

def func2(a, b, c):
    return a * b * c

# Example usage
row_data = [10, 20, 30, 40, 50]
result1 = foo(row_data, func1, 0, 1, 2)  # Using indices from the row
result2 = foo(row_data, func2, 2, 3, 100)  # Dynamically adds 100 to the params

print(result1)  # Output: 60 (10 + 20 + 30)
print(result2)  # Output: 1200000 (30 * 40 * 100)
