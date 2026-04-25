
from itertools import product

def foo(nums):
    # Generate tuples of the positive and negative options for each number
    options = [[abs(num), -abs(num)] for num in nums]

    # Use itertools.product to create combinations of each number's positive and negative options
    combinations = list(product(*options))

    return combinations

# Test cases
print(foo([-4]))         # [[4], [-4]]
print(foo([1, 1]))       # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))      # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))   # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1],
                           #  [1, 1, 1], [1, 1, -1], [-1, 1, 1], [-1, 1, -1]]
