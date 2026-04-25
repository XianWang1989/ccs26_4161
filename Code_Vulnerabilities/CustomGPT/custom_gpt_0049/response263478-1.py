
def foo(row, f, **kwargs):
    if callable(f):
        # Prepare arguments to pass to function
        args = []
        for key, value in kwargs.items():
            if isinstance(value, int):
                args.append(row[value])  # Get value from row by index
            else:
                args.append(value)  # Use provided static arguments
        return f(*args)
    return f  # If f is not callable, just return it

# Example usage
def func1(a, b, c):
    return a + b + c

row = [10, 20, 30, 40, 50]  # Example dataset

# Now you can call foo with dynamic arguments from row and static ones
result = foo(row, func1, a=1, b=0, c=4)  # Passes row[1], row[0], row[4] to func1
print(result)  # Output: 10 + 20 + 50 = 80
