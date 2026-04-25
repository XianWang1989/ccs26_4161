
from itertools import product

def foo(nums):
    # Create a list of tuples with positive and negative values
    signs = [[abs(num), -abs(num)] for num in nums]

    # Use itertools.product to get all combinations of signs
    possibilities = list(product(*signs))

    # Convert tuples to lists
    return [list(possibility) for possibility in possibilities]

# Test cases
print(foo([-4]))                # Expected output: [[4], [-4]]
print(foo([1, 1]))              # Expected output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))             # Expected output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))          # Expected output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, 1], [1, 1, -1], [-1, 1, 1], [-1, 1, -1]]

# More complex cases
print(foo([1, -1, 1]))          # Expected output variations for more complex cases
print(foo([1, -1, -1]))         # etc.
