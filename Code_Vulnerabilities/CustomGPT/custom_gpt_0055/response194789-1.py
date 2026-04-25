
import itertools

def foo(numbers):
    # Create a list of options for each number
    options = [[abs(num), -abs(num)] for num in numbers]

    # Use itertools.product to generate all combinations
    combinations = itertools.product(*options)

    # Convert the combinations to a list
    return [list(combination) for combination in combinations]

# Example usage:
print(foo([-4]))                          # [[4], [-4]]
print(foo([1, 1]))                        # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))                      # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))                   # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, 1], [1, 1, -1]]
