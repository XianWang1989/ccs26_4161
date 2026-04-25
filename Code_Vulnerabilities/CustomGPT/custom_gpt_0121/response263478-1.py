
class FunctionSpec:
    def __init__(self, func, *args):
        self.func = func
        self.args = args

def foo(row, spec):
    # Extract function and arguments from the spec
    func = spec.func
    args = []

    for arg in spec.args:
        if isinstance(arg, int):  # If it's an index, get from row
            args.append(row[arg])
        else:  # Otherwise, it's a static argument
            args.append(arg)

    return func(*args)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

# Example usage
fList = [
    FunctionSpec(func1, 0, 1, 4),  # Passes row[0], row[1], and static 4
    FunctionSpec(func2, 2)         # Passes row[2]
]

# Sample row
row = [10, 20, 30, 40, 50]

# Running foo with examples
for spec in fList:
    print(foo(row, spec))
