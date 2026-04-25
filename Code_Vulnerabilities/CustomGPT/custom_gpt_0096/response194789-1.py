
from itertools import product

def foo(numbers):
    # Generate a list of signs for each number
    signs = [[abs(num), -abs(num)] for num in numbers]

    # Use itertools.product to get all combinations of the signs
    combinations = list(product(*signs))

    return combinations

# Example usage
print(foo([-4]))        # [[4], [-4]]
print(foo([1, 1]))      # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))     # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))  # [[1, -1, 1], [1, -1, -1], ...]
