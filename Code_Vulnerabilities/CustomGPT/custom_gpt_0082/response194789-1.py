
from itertools import product

def foo(numbers):
    # Generate signs for each number
    signs = [[abs(num), -abs(num)] for num in numbers]

    # Use product to get all combinations of positive and negative
    combinations = list(product(*signs))

    return combinations

# Example usage
print(foo([-4]))  # Output: [[4], [-4]]
print(foo([1, 1]))  # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))  # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))  # Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], ...]
