
import itertools

def foo(numbers):
    # Create a list of possibilities for each number
    possibilities = [[abs(num), -abs(num)] for num in numbers]

    # Use itertools.product to get the Cartesian product of possibilities
    all_combinations = list(itertools.product(*possibilities))

    return all_combinations

# Example usages
print(foo([-4]))           # [[4], [-4]]
print(foo([1, 1]))         # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))        # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))     # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]

# Test case with multiple signs
print(foo([1, -1, 1]))     # Expecting combinations of [+,-,+]
