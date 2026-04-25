
from itertools import product

def foo(arr):
    # Generate a list of tuples containing both positive and negative variants of each number
    variants = [[abs(num), -abs(num)] for num in arr]

    # Use product to create all combinations of those variants
    result = list(product(*variants))

    # Convert tuples to lists for the final output
    return [list(combination) for combination in result]

# Test cases
print(foo([-4]))           # [[4], [-4]]
print(foo([1, 1]))        # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))       # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))    # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]
print(foo([-1, 3, -2]))   # [[1, 3, 2], [1, 3, -2], [1, -3, 2], [1, -3, -2], [-1, 3, 2], [-1, 3, -2], [-1, -3, 2], [-1, -3, -2]]
