
from itertools import product

def foo(numbers):
    # Create tuples of positive and negative versions of each number
    possibilities = [(abs(num), -abs(num)) for num in numbers]

    # Generate combinations using itertools.product
    combinations = list(product(*possibilities))

    return [list(combo) for combo in combinations]

# Example usage
print(foo([-4]))          # [[4], [-4]]
print(foo([1, 1]))        # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))       # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))    # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], ...]
