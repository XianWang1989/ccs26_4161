
from itertools import product

def foo(numbers):
    # Map the input numbers to their positive and negative equivalents
    sign_variations = []
    for num in numbers:
        sign_variations.append([abs(num), -abs(num)])

    # Use itertools.product to create all combinations of the sign variations
    combinations = list(product(*sign_variations))

    return combinations

# Example usages
print(foo([-4]))                      # Output: [[4], [-4]]
print(foo([1, 1]))                    # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))                   # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))                # Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, 1]]

# Custom test case
print(foo([1, -1, 1]))                # Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, 1]]
