
from itertools import product

def foo(nums):
    # Generate combinations of '+' and '-' for the input numbers
    signs = [[abs(num), -abs(num)] for num in nums]
    combinations = list(product(*signs))
    return [list(combo) for combo in combinations]

# Test cases
print(foo([-4]))              # [[4], [-4]]
print(foo([1, 1]))            # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))           # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))        # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], ...]
