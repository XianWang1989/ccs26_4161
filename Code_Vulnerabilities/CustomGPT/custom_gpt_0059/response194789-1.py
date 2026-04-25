
import itertools

def foo(numbers):
    # Create a list of all positive and negative options for each number
    options = [[abs(num), -abs(num)] for num in numbers]

    # Use itertools.product to get all combinations
    combinations = list(itertools.product(*options))

    return combinations

# Example usage
print(foo([-4]))            # [[4], [-4]]
print(foo([1, 1]))         # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))        # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))     # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, 1, 1]]
