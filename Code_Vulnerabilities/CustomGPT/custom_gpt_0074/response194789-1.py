
from itertools import product

def foo(numbers):
    # Create a list of possible signs for each number
    possibilities = [[abs(num), -abs(num)] for num in numbers]

    # Use itertools.product to generate combinations of signs
    return [list(poss) for poss in product(*possibilities)]

# Example usage:
print(foo([-4]))
# Output: [[4], [-4]]

print(foo([1, 1]))
# Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]

print(foo([-1, 3]))
# Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]

print(foo([1, -1, 1]))
# Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [1, 1, 1], [-1, 1, -1], [-1, 1, 1]]
