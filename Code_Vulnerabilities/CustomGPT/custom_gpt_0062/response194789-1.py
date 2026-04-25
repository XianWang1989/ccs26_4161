
from itertools import product

def foo(arr):
    # Create a list of symbols (+, -) for each number in the input list
    options = []
    for num in arr:
        options.append([abs(num), -abs(num)])  # Using absolute value for flexibility

    # Generate all combinations of positive and negative numbers
    result = list(product(*options))

    return result

# Example usages
print(foo([-4]))
print(foo([1, 3]))
print(foo([1, -3]))
print(foo([-1, 3]))
print(foo([1, -1, 1]))
