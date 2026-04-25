
from itertools import product

def foo(lst):
    # Create a list of tuples with positive and negative variations
    variations = [(abs(num), -abs(num)) for num in lst]

    # Generate all combinations using product
    all_combinations = list(product(*variations))

    return all_combinations

# Example usage
print(foo([-4]))  # Output: [(4,), (-4,)]
print(foo([1, 1]))  # Output: [(1, 1), (1, -1), (-1, 1), (-1, -1)]
print(foo([-1, 3]))  # Output: [(1, 3), (1, -3), (-1, 3), (-1, -3)]
print(foo([1, -1, 1]))  # Output: [(1, -1, 1), (1, -1, -1), (-1, -1, 1), (-1, -1, -1), (1, 1, 1), (1, 1, -1), (-1, 1, 1), (-1, 1, -1)]
