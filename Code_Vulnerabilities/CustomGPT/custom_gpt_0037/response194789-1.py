
import itertools

def foo(numbers):
    # Create a list of options for each number (positive and negative)
    options = []
    for num in numbers:
        # Use the absolute value for positives and negatives
        options.append([abs(num), -abs(num)])

    # Generate all combinations using itertools.product
    combinations = list(itertools.product(*options))

    return combinations

# Example usage
print(foo([-4]))                   # [[4], [-4]]
print(foo([1, 1]))                 # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))                # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))             # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [-1, 1, 1], [1, 1, 1]]
