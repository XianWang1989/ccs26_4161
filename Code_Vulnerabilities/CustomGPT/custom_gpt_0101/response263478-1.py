
def foo(row, f, *args):
    if isinstance(f, str):
        return f
    elif isinstance(f, int):
        return row[f]
    else:
        return f(*[row[i] if isinstance(i, int) else i for i in args])

# Example usage
def func1(a, b, static):
    return a + b + static

def func2(x):
    return x * 2

fList = [
    (func1, 1, 0, 10),  # func1 with elements from row 1 and 0, and static argument 10
    (func2, 2),         # func2 with element from row 2
    "Hello, World",
    2                   # direct row access
]

row_data = [3, 4, 5]

# Example calls
result1 = foo(row_data, *fList[0])
result2 = foo(row_data, *fList[1])
result3 = foo(row_data, fList[2])
result4 = foo(row_data, fList[3])

print(result1)  # Outputs 17 (4 + 3 + 10)
print(result2)  # Outputs 10 (5 * 2)
print(result3)  # Outputs "Hello, World"
print(result4)  # Outputs 5 (element at index 2)
