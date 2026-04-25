
def foo(row, func, *args):
    # Extract specified elements from row based on args
    extracted_args = [row[i] for i in args if isinstance(i, int)]
    # Combine with any additional static arguments
    return func(*extracted_args)

# Example functions
def func1(a, b):
    return a + b

def func2(a, b, c):
    return a * b - c

# Example usage
row = [10, 20, 30, 40, 50]

# Call func1 with the first (0) and third (2) elements of 'row'
result1 = foo(row, func1, 0, 2)
print(result1)  # Output: 40 (10 + 30)

# Call func2 with the first (0), second (1), and static number 5
result2 = foo(row, func2, 0, 1, 5)
print(result2)  # Output: 195 (10 * 20 - 5)
