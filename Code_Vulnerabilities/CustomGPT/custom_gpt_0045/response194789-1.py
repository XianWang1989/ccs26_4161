
from itertools import product

def foo(nums):
    # Generate the positive and negative possibilities using product
    possibilities = product(*[ [abs(num), -abs(num)] for num in nums ])
    # Convert the tuples to lists
    return [list(possibility) for possibility in possibilities]

# Testing the function with given examples
print(foo([-4]))
# Output: [[4], [-4]]

print(foo([1, 1]))
# Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]

print(foo([-1, 1]))
# Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]

print(foo([-1, 3]))
# Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]

print(foo([1, -1, 1]))
# Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1],[-1, -1, -1], [1, 1, -1], [1, 1, 1], [-1, 1, 1], [-1, 1, -1]]
