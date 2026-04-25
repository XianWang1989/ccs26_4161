
from itertools import product

def foo(nums):
    # Generate possibilities using product for all combinations of positive and negative
    return [[sign for sign in signs] for signs in product(*[[abs(num), -abs(num)] for num in nums])]

# Examples
print(foo([-4]))          # [[4], [-4]]
print(foo([1, 1]))        # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))       # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))    # [[-1, -1, -1], [-1, -1, 1], [-1, 1, -1], [-1, 1, 1], [1, -1, -1], [1, -1, 1], [1, 1, -1], [1, 1, 1]]
