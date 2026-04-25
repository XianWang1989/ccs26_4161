
def foo(row, func_desc):
    func = func_desc[0]
    # Extract row elements based on specified indices
    row_args = [row[i] for i in func_desc[1]]  # Function arguments from row
    # Extract any static arguments (from the third element onward)
    static_args = func_desc[2:] if len(func_desc) > 2 else []
    return func(*row_args, *static_args)  # Call the function

# Example functions
def func1(a, b, c, d=0):
    return a + b + c + d

def func2(x):
    return x * 2

# Example function list
fList = [
    (func1, [1, 0, 4], 10),  # func1 with row elements at indices 1, 0, 4 and static arg 10
    (func2, [2]),           # func2 with row element at index 2
    'Hello, World',        # Direct string
    (func1, [0, 3], 5)     # Another example of func1 with different arguments
]

# Example row
row = [3, 5, 10, 0, 7]

# Running the functions
results = [foo(row, f) for f in fList]
print(results)
