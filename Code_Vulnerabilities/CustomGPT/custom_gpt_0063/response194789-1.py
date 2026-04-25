
from itertools import product

def foo(numbers):
    # Create a list of tuples representing the positive and negative versions of each number
    possibilities = [(abs(num), -abs(num)) for num in numbers]

    # Generate all combinations using the Cartesian product
    result = list(product(*possibilities))

    return result

# Example usage
print(foo([-4]))              # [[4], [-4]]
print(foo([1, 1]))           # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))         # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))      # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], ...]
