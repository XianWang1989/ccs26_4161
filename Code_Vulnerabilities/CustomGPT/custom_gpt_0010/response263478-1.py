
def foo(row, f):
    # Check if f is a string or int
    if isinstance(f, str):  # Return string directly
        return f
    elif isinstance(f, int):  # Return the element at the index from the row
        return row[f]

    # If f is a function with specified arguments
    func, *args = f

    # Prepare the arguments for the function
    call_args = []
    for arg in args:
        if isinstance(arg, int):  # Index reference from the row
            call_args.append(row[arg])
        elif isinstance(arg, str):  # Static string arguments
            call_args.append(arg)  
        else:
            raise ValueError("Arguments must be integers (indices) or strings.")

    return func(*call_args)  # Call the function with the prepared arguments

# Sample functions for demonstration
def func1(a, b):
    return a + b

def func2(x):
    return f"Value: {x}"

def func3(s1, s2):
    return f"{s1} and {s2}"

# Example usage
row = [10, 20, 30, 40, 50]
fList = [
    (func1, 0, 1),          # func1 with row[0] and row[1]
    (func2, 2),             # func2 with row[2]
    (func3, 3, 'is awesome')  # func3 with row[3] and static string
]

for f in fList:
    print(foo(row, f))  # Outputs results of function calls
