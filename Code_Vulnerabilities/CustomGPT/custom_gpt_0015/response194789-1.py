
import itertools

def foo(numbers):
    # Create a list of possible signs for each number
    sign_combinations = list(itertools.product([-1, 1], repeat=len(numbers)))

    # Generate combinations based on the signs
    result = [[sign * num for sign, num in zip(combination, numbers)] for combination in sign_combinations]

    return result

# Example usages
print(foo([-4]))               # [[4], [-4]]
print(foo([1, 1]))            # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))           # [[-1, 3], [-1, -3], [1, 3], [1, -3]]
print(foo([1, -1, 1]))        # [[1, -1, 1], [1, 1, 1], [-1, -1, 1], [-1, 1, -1], [1, -1, -1], [-1, 1, 1]]

# Testing with mixed signs
print(foo([1, -1, 1]))        # [[1, -1, 1], [1, 1, 1], [-1, -1, 1], [-1, 1, -1], [1, -1, -1], [-1, 1, 1]]
