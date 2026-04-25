
def foo(row, f, *args, **kwargs):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        # Extract the arguments from row based on their indices
        args_from_row = [row[i] for i in args if isinstance(i, int)]
        return f(*args_from_row, **kwargs)

# Example functions
def func1(a, b):
    return a + b

def func2(x, static=0):
    return x + static

def func3(item1, item2):
    return f"{item1} and {item2}"

# Example row and function list
row = [10, 20, 30, 40, 50]

# Function calls
print(foo(row, func1, 0, 1))  # Outputs: 30 (10 + 20)
print(foo(row, func2, 2, static=5))  # Outputs: 35 (30 + 5)
print(foo(row, func3, 3, 4))  # Outputs: "40 and 50"
print(foo(row, "Hello, World"))  # Outputs: "Hello, World"
print(foo(row, 2))  # Outputs: 30 (value at index 2)
