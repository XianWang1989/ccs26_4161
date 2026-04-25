
def foo(row, f):
    # If the input is a string, return it directly
    if isinstance(f, str):
        return f

    # If the input is an instance of int or long, return the corresponding element from the row
    elif isinstance(f, int):
        return row[f]

    # If the input is a function (or a callable), extract its parameters
    elif callable(f):
        return f(**{k: row[v] for k, v in f.__annotations__.items()})

# Example functions with annotations
def func1(a: int, b: int) -> int:
    return a + b

def func2(x: str) -> str:
    return f"Hello {x}"

def func3(count: int, message: str) -> str:
    return f"{message} " * count

# Create a sample fList that maps function names and their expected arguments
fList = [
    (func1, {'a': 0, 'b': 1}),          # Maps 'a' to index 0 and 'b' to index 1 of row
    (func2, {'x': 2}),                  # Maps 'x' to index 2 of row
    (func3, {'count': 3, 'message': 4}) # Maps 'count' to index 3 and 'message' to index 4
]

# Example row
row = [1, 2, 'World', 3, 'spam']

# Evaluate the functions
results = [foo(row, f[0])(row=f[1]) for f in fList]

print(results) # Output will show results from each function call
