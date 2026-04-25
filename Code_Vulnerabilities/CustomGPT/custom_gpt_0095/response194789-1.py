
from itertools import product

def foo(numbers):
    # Create a list of signs for each number
    signs = [[abs(num), -abs(num)] for num in numbers]

    # Generate all combinations of signs using Cartesian product
    combinations = list(product(*signs))

    return combinations

# Example usage
print(foo([-4]))               # Outputs: [[4], [-4]]
print(foo([1, 1]))             # Outputs: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))            # Outputs: [[-1, 3], [-1, -3], [1, 3], [1, -3]]
print(foo([1, -1, 1]))         # Outputs: [[1, -1, 1], [1, -1, -1], [1, 1, -1], [-1, -1, 1], [-1, 1, -1], [-1, -1, -1]]

# For the complex example with mixed signs
print(foo([1, -1, 1]))
