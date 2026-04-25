
from itertools import product

def foo(numbers):
    # Create a list of tuples with positive and negative variations
    possibilities = [[abs(num), -abs(num)] for num in numbers]

    # Use itertools.product to get all combinations of the variations
    result = list(product(*possibilities))

    return result

# Example usage
print(foo([-4]))                # [[4], [-4]]
print(foo([1, 1]))              # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))             # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))          # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]
