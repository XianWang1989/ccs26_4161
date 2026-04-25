
def foo(row, func_spec):
    if isinstance(func_spec, str):
        return func_spec  # If it's a string, return it directly
    elif isinstance(func_spec, int):
        return row[func_spec]  # If it's an integer, return the corresponding row element
    elif callable(func_spec):
        return func_spec()  # Call the function if it's callable
    else:
        func, *args = func_spec  # Unpack the function and its arguments
        resolved_args = [arg if not isinstance(arg, int) else row[arg] for arg in args]
        return func(*resolved_args)  # Call the function with resolved arguments

# Example Functions
def func1(a, b):
    return a + b

def func2(x):
    return f"Value: {x}"

# Example Data Row
row_data = [10, 20, 30, 40, 50]

# Function Specifications
fList = [
    (func1, 0, 1),  # Adding row[0] and row[1]
    (func2, 3),    # Applying func2 to row[3]
    'Hello, World',  # A plain string
    2               # Accessing row[2]
]

# Execute
for f in fList:
    print(foo(row_data, f))
