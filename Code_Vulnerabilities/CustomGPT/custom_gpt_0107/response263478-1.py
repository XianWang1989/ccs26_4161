
def foo(row, spec):
    func = spec['function']
    args = []

    for arg in spec['args']:
        if isinstance(arg, str):  # Look it up in row
            args.append(row[int(arg)])  # Assuming row has indices as strings
        elif isinstance(arg, (int, float)):  # Static arguments
            args.append(arg)
        else:
            raise ValueError("Invalid argument type.")

    return func(*args)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

# Example usage
row = [1, 2, 3, 4, 5]  # Sample data

fList = [
    {'function': func1, 'args': ['1', 10, '0']},  # Will pass row[1], 10, row[0]
    {'function': func2, 'args': ['2']}            # Will pass row[2]
]

for f in fList:
    print(foo(row, f))  # Outputs results based on the specified functions and arguments
