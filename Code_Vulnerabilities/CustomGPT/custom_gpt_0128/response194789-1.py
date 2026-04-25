
import itertools

def foo(nums):
    # Generate combinations of positive and negative signs
    sign_combinations = list(itertools.product([-1, 1], repeat=len(nums)))

    # Calculate the resulting lists based on combinations
    results = [[num * sign for num, sign in zip(nums, signs)] for signs in sign_combinations]

    return results

# Example usages
print(foo([-4]))             # [[4], [-4]]
print(foo([1, 1]))          # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))        # [[-1, 3], [-1, -3], [1, 3], [1, -3]]
print(foo([1, -1, 1]))     # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, 1, -1], [1, 1, -1], [1, -1, -1], [-1, 1, 1], [-1, -1, 1]]
