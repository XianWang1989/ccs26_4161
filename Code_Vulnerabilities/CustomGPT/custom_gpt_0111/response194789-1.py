
from itertools import product

def foo(lst):
    # Generate all combinations of positive and negative signs
    signs = list(product([1, -1], repeat=len(lst))
    result = [[sign * abs(num) for sign, num in zip(combination, lst)] for combination in signs]
    return result

# Example usages:
print(foo([-4]))
# Output: [[4], [-4]]

print(foo([1, 1]))
# Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]

print(foo([-1, 3]))
# Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]

print(foo([1, -1, 1]))
# Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [-1, 1, -1], [1, 1, 1], [-1, 1, 1]]
