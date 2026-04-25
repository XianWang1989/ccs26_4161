
def foo(row, func, *args):
    """
    Calls the specified function with row elements and additional static arguments.

    :param row: A list or tuple containing data elements
    :param func: The function to call
    :param args: Additional static arguments to pass to the function
    :return: Result of the function call
    """
    return func(*args, *[row[i] for i in args if isinstance(i, int)])

def func1(a, b, c):
    return a + b + c

def func2(x, y):
    return x * y

# Example usage
row = [10, 20, 30, 40, 50]

# Example 1: Call func1 with specific elements from row and a static integer
result1 = foo(row, func1, 0, 1, 2)  # This will compute func1(10, 20, 30)
print(result1)  # Output: 60

# Example 2: Call func2 with elements and static arguments
result2 = foo(row, func2, 1, 3, 5)  # This will compute func2(20, 40)
print(result2)  # Output: 800

# Example 3: Call a function with only static arguments
def func3(message):
    return message

result3 = foo(row, func3, 'Hello, World')
print(result3)  # Output: Hello, World
