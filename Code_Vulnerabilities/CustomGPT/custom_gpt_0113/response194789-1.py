
from itertools import product

def foo(numbers):
    # Create a list of lists with positive and negative versions of each number
    options = [[n, -n] for n in numbers]

    # Use itertools.product to generate all combinations
    combinations = list(product(*options))

    return combinations

# Example usage:
print(foo([-4]))  # Output: [[4], [-4]]
print(foo([1, 2]))  # Output: [[1, 2], [1, -2], [-1, 2], [-1, -2]]
print(foo([-1, 3]))  # Output: [[-1, 3], [-1, -3], [1, 3], [1, -3]]
print(foo([1, -1]))  # Output: [[1, -1], [1, 1], [-1, -1], [-1, 1]]
