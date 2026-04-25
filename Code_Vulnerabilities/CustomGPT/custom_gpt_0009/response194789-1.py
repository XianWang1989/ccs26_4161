
from itertools import product

def foo(nums):
    # Generate combinations of signs for each number
    possibilities = product(*( [abs(num), -abs(num)] for num in nums ))
    return [list(possibility) for possibility in possibilities]

# Example usage
print(foo([-4]))         # [[4], [-4]]
print(foo([1, 1]))       # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))      # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))   # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, 1, 1], [1, 1, -1], [-1, 1, -1]]
