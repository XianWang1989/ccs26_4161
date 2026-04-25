
def foo(row, f, **kwargs):
    # Check if f is a function
    if callable(f):
        return f(**{**kwargs, **{key: row[index] for key, index in kwargs.items()}})
    # If f is a string or int, handle accordingly
    elif isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        raise ValueError("Unsupported function type")

# Example functions
def func1(a, b):
    return a + b

def func2(x):
    return x * 2

# Example usage
row = [10, 20, 30, 40]

# Specify the row elements and static arguments
result = foo(row, func1, a=1, b=2)  # dynamic use of row elements
print(result)  # Output: 3

result_static = foo(row, func2, x=2)  # Static argument use
print(result_static)  # Output: 4

result_string = foo(row, "Hello, World")
print(result_string)  # Output: Hello, World

result_int = foo(row, 1)  # Access row element directly
print(result_int)  # Output: 20
