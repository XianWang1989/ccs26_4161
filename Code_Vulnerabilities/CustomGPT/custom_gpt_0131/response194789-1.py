
from itertools import product

def foo(numbers):
    # Generate combinations of positive and negative values
    combinations = [[sign for sign in signs] for signs in product(*[[abs(num), -abs(num)] for num in numbers])]
    return combinations

# Example usage
print(foo([-4]))          # [[4], [-4]]
print(foo([1, 1]))       # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))      # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1]))      # [[1, -1], [1, 1], [-1, -1], [-1, 1]]
print(foo([1, -3, 2]))   # Outputs all combinations of + and - for the given list
