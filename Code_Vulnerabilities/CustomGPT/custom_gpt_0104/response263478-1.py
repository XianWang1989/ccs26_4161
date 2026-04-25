
def foo(row, f):
    if callable(f):  # Check if f is a callable (function)
        return f(*row)  # Pass the whole row to the function

    return f  # If it's not callable, just return the value

# Example functions
def func1(a, b, c):
    return a + b - c

def func2(x, y):
    return x * y

def func3(msg1, msg2):
    return f"{msg1}, {msg2}!"

# Using a dictionary for mapping
def apply_functions(row, fList):
    results = []
    for f, args in fList:
        # Extract the arguments based on the provided indices or values
        extracted_args = [row[arg] if isinstance(arg, int) else arg for arg in args]
        results.append(foo(extracted_args, f))
    return results

# Example data row
data_row = [10, 5, 2]

# Using the function list
fList = [
    (func1, [0, 1, 2]),  # using indices from data_row
    (func2, [0, 1]),     # using indices from data_row
    (func3, ['Spam', 'Eggs']),  # static arguments
]

# Apply the functions
results = apply_functions(data_row, fList)

# Output the results
print(results)  # Output: [13, 50, 'Spam, Eggs!']
