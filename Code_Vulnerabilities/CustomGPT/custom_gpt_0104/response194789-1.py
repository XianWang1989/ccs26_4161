
from itertools import product

def foo(arr):
    # Create a sign version of each element in arr
    signs = [[abs(num), -abs(num)] for num in arr]

    # Generate all combinations using product
    combinations = list(product(*signs))

    return combinations

# Example usage
print(foo([-4]))           # [[4], [-4]]
print(foo([1, 1]))        # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))       # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))    # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [1, 1, 1], [-1, 1, -1], [-1, 1, 1]]
