
def foo(row, spec):
    if isinstance(spec, str):
        return spec  # Return the string as is
    elif isinstance(spec, int):
        return row[spec]  # Return the element at index `spec`
    elif isinstance(spec, dict):
        func = spec['function']
        args = spec.get('args', [])
        # Resolve row elements by index or name
        resolved_args = []
        for arg in args:
            if isinstance(arg, int):  # Index from the row
                resolved_args.append(row[arg])
            elif isinstance(arg, str):  # Support for string keys (if using dict-like rows)
                resolved_args.append(row.get(arg, None))
            else:
                resolved_args.append(arg)  # Static arguments

        return func(*resolved_args)  # Call the user-defined function with resolved arguments
    return None  # Handles cases that don't match

# Example functions
def func1(a, b):
    return a + b

def func2(x):
    return x * 2

# Example fList
fList = [
    {'function': func1, 'args': [1, 2]},  # Will use values from row at index 1 and 2
    {'function': func2, 'args': [5]},      # Will use 5 directly
    'Hello, World',
    0                                 # Returns the first element of the row
]

# Sample data row
row = [10, 20, 30, 40]

# Using foo with different specs
for spec in fList:
    print(foo(row, spec))  # Will output values based on the specs
