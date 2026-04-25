
from itertools import product

def foo(nums):
    # Create the lists of possibilities for each number
    possibilities = [[abs(num), -abs(num)] for num in nums]

    # Generate all combinations using the Cartesian product
    return list(product(*possibilities))

# Example usage:
print(foo([-4]))               # [[4], [-4]]
print(foo([1, 1]))            # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))           # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))        # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, 1], [1, 1, -1], [-1, 1, 1], [-1, 1, -1]]
