
class FunctionWrapper:
    def __init__(self, func, indices=None, *args):
        self.func = func
        self.indices = indices if indices is not None else []
        self.args = args

    def __call__(self, row):
        # Collect the relevant elements from the row
        row_elements = [row[i] for i in self.indices]
        # Combine row elements with static arguments
        all_args = row_elements + list(self.args)
        return self.func(*all_args)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

def func3(a, b):
    return f"{a} and {b}"

# Usage
row = [1, 2, 3, 4, 5]
fList = [
    FunctionWrapper(func1, [0, 1, 2]),
    FunctionWrapper(func2, [3]),
    FunctionWrapper(func3, [0, 1], 'static1', 'static2')
]

# Demonstration of foo function
def foo(row, wrapped_func):
    return wrapped_func(row)

# Testing the functions in fList
for wrapped_function in fList:
    print(foo(row, wrapped_function))
