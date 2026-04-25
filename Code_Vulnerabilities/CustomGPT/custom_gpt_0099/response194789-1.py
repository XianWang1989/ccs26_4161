
from itertools import product

def foo(lst):
    # Create a list of tuples with + and - for each number
    possibilities = [[abs(num), -abs(num)] for num in lst]
    # Use product to get all combinations of the tuples
    return [list(comb) for comb in product(*possibilities)]

# Test cases
print(foo([-4])) # Output: [[4], [-4]]
print(foo([1, 1])) # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3])) # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1])) # Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]
