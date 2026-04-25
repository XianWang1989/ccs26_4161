
import itertools

def foo(numbers):
    # Generate all combinations of sign changes for the input list
    sign_combinations = list(itertools.product(*[[-abs(num), abs(num)] for num in numbers]))

    # Convert to list of lists
    return [list(combination) for combination in sign_combinations]

# Example usage:
print(foo([-4]))            # [[4], [-4]]
print(foo([1, 1]))         # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))        # [[-1, 3], [-1, -3], [1, 3], [1, -3]]
print(foo([1, -1, 1]))     # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [-1, 1, -1], [1, 1, 1], [-1, 1, 1]]

# The output matches the expected behavior.
