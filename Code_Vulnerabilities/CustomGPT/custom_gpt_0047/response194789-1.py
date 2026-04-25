
from itertools import product

def foo(numbers):
    # Create a list of tuples for positive and negative values
    possibilities = [(abs(num), -abs(num)) for num in numbers]

    # Generate all combinations of positive and negative values using product
    combinations = list(product(*possibilities))

    # Convert tuples to lists for the final output
    return [list(combination) for combination in combinations]

# Example usage
print(foo([-4]))              # [[4], [-4]]
print(foo([1, 1]))            # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))           # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))        # [[-1, -1, 1], [-1, 1, 1], [1, -1, 1], [1, 1, 1], [-1, -1, -1], [-1, 1, -1], [1, -1, -1], [1, 1, -1]]

