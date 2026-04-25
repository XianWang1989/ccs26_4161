
from itertools import product

def foo(nums):
    # Create a list of signs for each number
    signs = [[abs(num), -abs(num)] for num in nums]

    # Use itertools.product to create all combinations of signs
    combinations = list(product(*signs))

    return combinations

# Example usage
print(foo([-4]))             # [[4], [-4]]
print(foo([1, 2]))           # [[1, 2], [1, -2], [-1, 2], [-1, -2]]
print(foo([1, -1]))          # [[1, -1], [1, 1], [-1, -1], [-1, 1]]
print(foo([-1, 3]))          # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))       # [[1, -1, 1], [1, 1, 1], [-1, -1, 1], [-1, 1, 1], 
                              #  [1, -1, -1], [1, 1, -1], [-1, -1, -1], [-1, 1, -1]]
