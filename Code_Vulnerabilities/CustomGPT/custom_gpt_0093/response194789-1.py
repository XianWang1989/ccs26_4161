
from itertools import product

def foo(numbers):
    # Create a list of tuples with positive and negative variants
    variants = [[abs(num), -abs(num)] for num in numbers]

    # Use product to create all combinations of positive and negative values
    combinations = list(product(*variants))

    return combinations

# Examples to demonstrate the function
print(foo([-4]))
print(foo([1, 1]))  # Replacing + with 1 for positive representation
print(foo([-1, 3]))
print(foo([1, -1, 1]))  # Replacing + and - with 1 and -1
