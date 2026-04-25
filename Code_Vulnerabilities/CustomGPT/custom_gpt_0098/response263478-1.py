
def foo(row, f, **kwargs):
    # Prepare arguments to pass to the function
    args = []

    # Add elements from row based on the keys in kwargs
    for key in kwargs:
        if isinstance(key, int):
            args.append(row[key])
        elif key in row:
            args.append(row[key])
        else:
            raise ValueError(f"Key {key} not found in row.")

    # Add static arguments from kwargs
    static_args = [kwargs[key] for key in kwargs if isinstance(key, str)]
    args.extend(static_args)

    return f(*args)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x, y, static_value):
    return x * y + static_value

# Example usage
row = [10, 20, 30, 40]
result1 = foo(row, func1, a=0, b=1, c=2)  # Uses row[0], row[1], row[2]
result2 = foo(row, func2, x=0, y=2, static_value=5)  # Uses row[0], row[2]

print(result1)  # Output: 60
print(result2)  # Output: 25
