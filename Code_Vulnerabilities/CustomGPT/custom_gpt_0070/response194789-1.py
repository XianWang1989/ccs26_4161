
import itertools

def foo(numbers):
    # Create a list of lists containing positive and negative versions of each number
    possibilities = [[abs(num), -abs(num)] for num in numbers]

    # Generate the Cartesian product of the possibilities
    all_combinations = list(itertools.product(*possibilities))

    return [list(combination) for combination in all_combinations]

# Examples
print(foo([-4]))                # Output: [[4], [-4]]
print(foo([1, 1]))              # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))             # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))          # Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], ...]

