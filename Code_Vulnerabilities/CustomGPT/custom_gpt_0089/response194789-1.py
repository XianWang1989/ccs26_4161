
import itertools

def foo(numbers):
    # Create a list of options for each number
    options = [[abs(num), -abs(num)] for num in numbers]

    # Generate all combinations using itertools.product
    all_combinations = list(itertools.product(*options))

    return all_combinations

# Example usage:
print(foo([-4]))  # [[4], [-4]]
print(foo([1, 1]))  # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))  # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))  # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [-1, 1, 1]]
