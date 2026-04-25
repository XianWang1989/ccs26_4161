
from itertools import product

def foo(numbers):
    # Create a list of tuples for the positive and negative versions of each number
    possibilities = [(abs(num), -abs(num)) for num in numbers]

    # Generate all combinations of the possibilities
    all_combinations = product(*possibilities)

    # Convert tuples to lists
    result = [list(combination) for combination in all_combinations]

    return result

# Example usage:
print(foo([-4]))            # [[4], [-4]]
print(foo([1, 1]))         # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))        # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))     # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, 1], [-1, 1, 1], [1, 1, -1], [-1, 1, -1]]

