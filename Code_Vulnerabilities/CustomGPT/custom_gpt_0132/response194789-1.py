
from itertools import product

def foo(numbers):
    # Map numbers to their positive and negative counterparts
    possibilities = [[abs(num), -abs(num)] for num in numbers]

    # Use itertools.product to create combinations
    combinations = list(product(*possibilities))

    return combinations

# Example usages
print(foo([-4]))         # Output: [[4], [-4]]
print(foo([1, 1]))       # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))      # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))   # Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]
