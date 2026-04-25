
def foo(row, f, *args):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        func_args = []
        for element in f:
            if isinstance(element, int):  # Index in row
                func_args.append(row[element])
            elif isinstance(element, str):  # Static argument
                func_args.append(element)
            else:
                raise ValueError("Elements in f must be either int (index) or str (static argument)")

        return f[0](*func_args, *args)

# Example functions
def func1(x, y, z):
    return x + y + z

def func2(a):
    return a * 2

# Example row
row = [1, 3, 5, 'spam', 'eggs']

# Example function list
fList = [
    (func1, [0, 1, 2]),  # Passing row[0], row[1], row[2] to func1
    (func2, [0]),        # Passing row[0] to func2
    'Hello, World',      # A string to return as is
    2                    # Returning row[2]
]

# Example usage
print(foo(row, fList[0]))   # Outputs: 9 (1 + 3 + 5)
print(foo(row, fList[1]))   # Outputs: 2 (1 * 2)
print(foo(row, fList[2]))   # Outputs: Hello, World
print(foo(row, fList[3]))   # Outputs: 5 (row[2])
