
from itertools import product

def foo(nums):
    # Create representation for each number
    options = []
    for num in nums:
        if num < 0:
            options.append([-abs(num), abs(num)])
        else:
            options.append([abs(num), -abs(num)])

    # Create all combinations of positive and negative
    combinations = list(product(*options))
    return combinations

# Example usage
print(foo([-4]))               # [[4], [-4]]
print(foo([1, 1]))            # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))           # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))        # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, 1, 1]]
