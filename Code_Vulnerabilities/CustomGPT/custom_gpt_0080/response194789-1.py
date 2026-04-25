
from itertools import product

def foo(numbers):
    # Create a list of options for each number (positive and negative)
    options = [[abs(num), -abs(num)] for num in numbers]

    # Use itertools.product to generate all combinations
    combinations = list(product(*options))

    return combinations

# Test cases
print(foo([-4]))         # [[4], [-4]]
print(foo([1, 1]))       # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))      # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))   # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [1, 1, 1], [-1, 1, 1], [-1, 1, -1]]
