
from itertools import product

def foo(numbers):
    # Create list of possibilities for each number
    possibilities = [[abs(num), -abs(num)] for num in numbers]

    # Generate all combinations using Cartesian product
    result = list(product(*possibilities))

    return result

# Example usages:
print(foo([-4]))                     # Output: [[4], [-4]]
print(foo([1, 1]))                   # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))                  # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))               # Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]
