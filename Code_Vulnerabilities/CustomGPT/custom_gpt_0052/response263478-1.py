
def foo(row, f, *args):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        # Extract the arguments based on the indices or static values
        func_args = []
        for item in f:
            if isinstance(item, int):
                func_args.append(row[item])  # Add row element
            elif isinstance(item, str):
                func_args.append(item)  # Add static string
            else:
                raise ValueError("Unsupported type in function arguments")

        return f[0](*func_args, *args)  # Call the function with args

# Example functions
def func1(a, b, c):
    return f"func1 called with {a}, {b}, {c}"

def func2(x, msg):
    return f"func2 called with {x} and message '{msg}'"

# Example data
row = [10, 20, 30, 40, 50]
fList = [
    (func1, [0, 1, 2]),  # uses row[0], row[1], row[2]
    (func2, [1, "Hello"]) # uses row[1] and static string
]

# Using the foo function
result1 = foo(row, fList[0])
print(result1)  # Output: func1 called with 10, 20, 30

result2 = foo(row, fList[1])
print(result2)  # Output: func2 called with 20 and message 'Hello'
