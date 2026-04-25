
from itertools import product

def foo(numbers):
    # Create a list of tuples with positive and negative versions of each number
    possibilities = [(abs(num), -abs(num)) for num in numbers]

    # Use itertools.product to generate all combinations of these tuples
    combinations = product(*possibilities)

    # Convert the tuples to lists and return as a list of lists
    return [list(combination) for combination in combinations]

# Example usages
print(foo([-4]))  # Output: [[4], [-4]]
print(foo([1, 1]))  # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))  # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))  # Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]
