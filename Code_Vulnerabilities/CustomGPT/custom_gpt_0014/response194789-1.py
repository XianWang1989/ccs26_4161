
import itertools

def foo(nums):
    # Create a list of sign options for each number in the input list
    sign_options = [[abs(num), -abs(num)] for num in nums]

    # Generate all combinations of signs
    combinations = list(itertools.product(*sign_options))

    return combinations

# Example usage
print(foo([-4]))            # Output: [[4], [-4]]
print(foo([1, 1]))         # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))        # Output: [[-1, 3], [-1, -3], [1, 3], [1, -3]]
print(foo([1, -1, 1]))     # Output: [[1, -1, 1], [1, -1, -1], [-1, 1, 1], [-1, 1, -1], [1, -1, 1], [-1, -1, 1], [1, 1, -1], [-1, -1, -1]]

# Testing with mixed signs
print(foo([1, -1, 1]))     # Output: All combinations with positive and negative
