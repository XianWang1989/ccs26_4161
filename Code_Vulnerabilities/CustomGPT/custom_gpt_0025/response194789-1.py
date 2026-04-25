
from itertools import product

def foo(numbers):
    # Generate combinations of positive and negative values for each number
    combinations = product(*[[abs(num), -abs(num)] for num in numbers])
    return [list(combo) for combo in combinations]

# Example usage
print(foo([-4]))           # [[4], [-4]]
print(foo([1, 1]))        # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))       # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))    # [[1, -1, 1], [1, -1, -1], [-1, 1, 1], [-1, 1, -1], [1, 1, -1], [-1, -1, 1], [-1, -1, -1], [-1, -1, 1]]
