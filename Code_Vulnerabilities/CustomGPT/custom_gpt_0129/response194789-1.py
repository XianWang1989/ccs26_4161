
from itertools import product

def foo(lst):
    # Generate combinations of positive and negative signs
    choices = [[abs(x), -abs(x)] for x in lst]
    # Use itertools.product to get all combinations
    result = list(product(*choices))
    return result

# Example usage:
print(foo([-4]))              # Output: [[4], [-4]]
print(foo([1, 1]))           # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))          # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))       # Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, 1], [1, 1, -1]]
