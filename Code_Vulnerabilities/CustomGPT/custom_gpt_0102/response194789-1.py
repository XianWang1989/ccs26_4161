
from itertools import product

def foo(numbers):
    # Create a list of tuples with positive and negative versions of each number
    variations = [(abs(num), -abs(num)) for num in numbers]

    # Generate all combinations using product
    combinations = list(product(*variations))

    return combinations

# Examples
print(foo([-4]))          # [[4], [-4]]
print(foo([1, 1]))        # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))       # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))    # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [-1, 1, -1], [1, 1, 1], [-1, 1, 1]]
