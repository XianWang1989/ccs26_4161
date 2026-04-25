
from itertools import product

def foo(numbers):
    # Create tuples of positive and negative variants for each number
    variants = [[abs(num), -abs(num)] for num in numbers]

    # Generate the Cartesian product of the variants
    combinations = product(*variants)

    # Convert tuples back to lists
    return [list(combination) for combination in combinations]

# Example usage
print(foo([-4]))                # [[4], [-4]]
print(foo([1, 1]))              # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))             # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))          # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [1, 1, 1]]
