
from itertools import product

def foo(int_list):
    # Create a list of signed variants for each number
    variants = [[abs(num), -abs(num)] for num in int_list]

    # Use itertools.product to generate all combinations
    combinations = list(product(*variants))

    return combinations

# Example usage
print(foo([-4]))
print(foo([1, 3]))
print(foo([1, -1]))
print(foo([-1, 3]))
print(foo([1, -1, 1]))
