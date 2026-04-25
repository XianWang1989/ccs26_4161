
from itertools import product

def foo(nums):
    # Create a list of lists for positive and negative counterparts
    options = [[abs(num), -abs(num)] for num in nums]

    # Generate all combinations using product
    combinations = list(product(*options))

    return combinations

# Test cases
print(foo([-4]))  # [[4], [-4]]
print(foo([1, 1]))  # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))  # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))  # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]
