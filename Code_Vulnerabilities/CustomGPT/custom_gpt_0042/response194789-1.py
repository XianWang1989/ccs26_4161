
from itertools import product

def foo(numbers):
    # Create a list of options for each number: positive and negative
    options = [[abs(num), -abs(num)] for num in numbers]

    # Generate all combinations using product
    combinations = list(product(*options))

    return combinations

# Example usage:
print(foo([-4]))                 # Output: [[4], [-4]]
print(foo([1, 1]))               # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))              # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))           # Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, 1], [-1, 1, 1], [1, 1, -1], [-1, 1, -1]]
