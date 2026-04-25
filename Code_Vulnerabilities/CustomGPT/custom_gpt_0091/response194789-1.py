
from itertools import product

def foo(numbers):
    # Create a list of possible signs for each number
    possibilities = [[abs(num), -abs(num)] for num in numbers]

    # Generate all combinations of these possibilities
    combinations = list(product(*possibilities))

    return combinations

# Example usage
print(foo([-4]))                  # [[4], [-4]]
print(foo([1, 1]))                # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))               # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))            # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [1, 1, 1], [-1, 1, 1], [-1, 1, -1]]
