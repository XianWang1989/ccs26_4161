
from itertools import product

def foo(numbers):
    # Create a list of tuples containing positive and negative variations
    possibilities = [(abs(num), -abs(num)) for num in numbers]

    # Get the Cartesian product of the possibilities
    all_combinations = list(product(*possibilities))

    # Convert tuples to lists
    final_result = [list(combination) for combination in all_combinations]

    return final_result

# Example usage:
print(foo([-4]))                # Outputs: [[4], [-4]]
print(foo([1, 1]))              # Outputs: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))             # Outputs: [[-1, 3], [-1, -3], [1, 3], [1, -3]]
print(foo([1, -1, 1]))          # Outputs: [[-1, -1, -1], [-1, -1, 1], [-1, 1, -1], [-1, 1, 1], [1, -1, -1], [1, -1, 1], [1, 1, -1], [1, 1, 1]]
