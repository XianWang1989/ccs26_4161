
def foo(row, f, *args, **kwargs):
    if callable(f):
        # Prepare the arguments to pass to the function
        func_args = [row[i] for i in kwargs.get('indices', [])] + list(args)
        return f(*func_args)
    elif isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        raise ValueError("Invalid function or index type.")

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

# Example data row
row = [10, 20, 30, 40, 50]

# Using foo
result1 = foo(row, func1, 100, indices=[0, 1, 2])  # Pass elements at index 0, 1, 2 from row plus 100
print(result1)  # Output: 160 (10 + 20 + 30 + 100)

result2 = foo(row, func2, indices=[4])  # Pass the element at index 4
print(result2)  # Output: 100 (50 * 2)

result3 = foo(row, "Hello, World")  # Simple string return
print(result3)  # Output: Hello, World

result4 = foo(row, 2)  # Pass an index directly
print(result4)  # Output: 30 (element at index 2)
