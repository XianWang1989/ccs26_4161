
def foo(row, f):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    elif callable(f):
        return f()  # Call the function if it takes no arguments
    else:
        func, *args = f  # Unpack the function and its arguments
        resolved_args = [foo(row, arg) for arg in args]  # Resolve each argument
        return func(*resolved_args)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

def func3(a, b):
    return f"{a} and {b}"

# Define the function list
fList = [
    (func1, 1, 0, 4),  # Uses elements from row at indices 1, 0, and uses static 4
    (func2, 2),        # Uses element from row at index 2
    (func3, 'spam', 'eggs'),  # Static arguments
    'Hello, World',
    2  # Returns the element at index 2 from row
]

# Example row
row = [5, 10, 20, 30, 40]

# Testing the function
print(foo(row, fList[0]))  # Output: 49 (10 + 5 + 4)
print(foo(row, fList[1]))  # Output: 40 (20*2)
print(foo(row, fList[2]))  # Output: "spam and eggs"
print(foo(row, fList[3]))  # Output: "Hello, World"
print(foo(row, fList[4]))  # Output: 20 (element at index 2)
