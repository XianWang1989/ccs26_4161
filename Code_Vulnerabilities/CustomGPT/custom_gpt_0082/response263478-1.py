
class Argument:
    def __init__(self, value):
        self.value = value

    def get_value(self, row):
        if isinstance(self.value, int):
            return row[self.value]
        elif callable(self.value):
            return self.value()
        else:
            return self.value

def foo(row, f):
    if isinstance(f, str):
        return f
    return f.get_value(row)

# Example functions
def func1(a, b, c):
    return a + b + c

def func2(x):
    return x * 2

fList = [
    (func1, [Argument(1), Argument(0), Argument(4)]),
    (func2, [Argument(2)]),
    Argument("Hello, World"),
    Argument(2)
]

# Execute foo with rows and functions
row = [10, 20, 30, 40, 50]
for func_data in fList:
    if isinstance(func_data, tuple):
        func, args = func_data
        print(func(*[foo(row, arg) for arg in args]))
    else:
        print(foo(row, func_data))
