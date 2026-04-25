
from itertools import product

def foo(nums):
    # Create a list of lists for positive and negative possibilities
    possibilities = [[abs(num), -abs(num)] for num in nums]
    # Generate all combinations using itertools.product
    return list(product(*possibilities))

# Example usage:
print(foo([-4]))               # Outputs: [(4,), (-4,)]
print(foo([1, 2]))            # Outputs: [(1, 2), (1, -2), (-1, 2), (-1, -2)]
print(foo([-1, 3]))           # Outputs: [(-1, 3), (-1, -3), (1, 3), (1, -3)]
print(foo([1, -1, 1]))        # Outputs: [(1, -1, 1), (1, -1, -1), (-1, -1, 1), (-1, 1, -1), (1, 1, 1), (1, 1, -1), (-1, 1, 1), (-1, -1, -1)]
