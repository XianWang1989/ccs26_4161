
def foo(row, f_spec):
    # If f_spec is just a string or an integer, return it directly
    if isinstance(f_spec, str):
        return f_spec
    elif isinstance(f_spec, int):
        return row[f_spec]

    # Extract the function and its parameters
    function = f_spec['func']
    args = []

    # Collect specified elements from the row
    for arg in f_spec.get('args', []):
        if isinstance(arg, int):  # if it's an index, get the value from row
            args.append(row[arg])
        elif isinstance(arg, str):  # if it's a static value, append it directly
            args.append(arg)

    return function(*args)

# Example functions for demonstration
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x ** 2

# Example usage
row_data = [10, 20, 30, 40, 50]

f_list = [
    {'func': func1, 'args': [0, 1, 3]},  # row[0] + row[1] + row[3]
    {'func': func2, 'args': [2]},         # square of row[2]
    'Hello, World',
    1                                    # returns row[1]
]

for f_spec in f_list:
    print(foo(row_data, f_spec))
