
import itertools

def foo(numbers):
    # Create a list of tuples containing both positive and negative options for each number
    options = [(abs(num), -abs(num)) for num in numbers]

    # Generate all combinations of the options using itertools.product
    combinations = list(itertools.product(*options))

    # Convert tuples to lists for the final output
    return [list(combination) for combination in combinations]

# Test examples
print(foo([-4]))  # Output: [[4], [-4]]
print(foo([1, 1]))  # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))  # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))  # Output: [[-1, -1, -1], [-1, -1, 1], [-1, 1, -1], [-1, 1, 1], [1, -1, -1], [1, -1, 1], [1, 1, -1], [1, 1, 1]]
