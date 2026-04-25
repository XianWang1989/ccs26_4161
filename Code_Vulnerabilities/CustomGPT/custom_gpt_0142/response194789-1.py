
from itertools import product

def foo(numbers):
    # Create a list of '+' and '-' for each number, resulting in [[$, -$] for each number]
    signs = [[abs(num), -abs(num)] for num in numbers] 

    # Use itertools.product to generate all combinations of signs
    combinations = product(*signs)

    # Convert the generator to a list
    return [list(combination) for combination in combinations]

# Example usages
print(foo([-4]))
# Output: [[4], [-4]]

print(foo([1, 1]))
# Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]

print(foo([-1, 3]))
# Output: [[-1, 3], [-1, -3], [1, 3], [1, -3]]

print(foo([1, -1, 1]))
# Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1],
#          [1, 1, 1], [1, 1, -1], [-1, 1, 1], [-1, 1, -1],
#          [1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]

# Test with a more complex case
print(foo([1, -1, 1]))
# Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1],
#          [1, 1, 1], [1, 1, -1], [-1, 1, 1], [-1, 1, -1],
#          [1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]
