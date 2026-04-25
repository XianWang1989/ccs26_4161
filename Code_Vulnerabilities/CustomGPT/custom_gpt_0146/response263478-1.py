
def foo(row, f):
    # Check if f is a string or an int and handle it accordingly
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]

    # Now we assume f is a dict with function mappings
    elif isinstance(f, dict):
        func = f.get('func')
        args = f.get('args', [])

        # Resolve actual arguments from row or static values
        resolved_args = []
        for arg in args:
            if isinstance(arg, int):  # Assume it’s an index
                resolved_args.append(row[arg])
            else:  # It’s a static value
                resolved_args.append(arg)

        # Call the function with resolved arguments
        return func(*resolved_args)

# Example functions
def func1(a, b, c):
    return a + b * c

def func2(x, y):
    return x ** y

# Example usage
row = [10, 20, 30, 40, 50]

# Function list using dictionary
fList = [
    {'func': func1, 'args': [1, 0, 4]},  # Reference to row: row[1], row[0], static 4
    {'func': func2, 'args': [0, 1]},      # Reference to row: row[0], static 1
    {'func': print, 'args': ['Hello, World']},  # Example with a print function and static argument
    {'func': lambda x: x + 2, 'args': [3]}  # An inline lambda with a static argument
]

for f in fList:
    result = foo(row, f)
    print('Result:', result)
