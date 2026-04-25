# Sample row
row = [10, 20, 30, 40, 50]

# Define functions
def func1(a, b, c): return a + b + c
def func2(*args): return sum(args)
def func3(spam, eggs): return f"{spam} and {eggs}"

# Function list with flexible callables
fList = [
    lambda row: func1(row[1], row[0], row[4]),
    lambda row: func2(*row[:10]),
    lambda row: func3("spam", "eggs"),
    lambda row: "Hello, World",
    lambda row: 2  # A static integer, not an index
]

# Generalized function caller
def foo(row, f):
    return f(row)

# Example usage
for f in fList:
    print(foo(row, f))
