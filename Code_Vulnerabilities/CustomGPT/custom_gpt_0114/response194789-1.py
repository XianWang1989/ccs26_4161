
import itertools

def foo(nums):
    # Create a list of tuples for each number, positive and negative
    possibilities = [(abs(num), -abs(num)) for num in nums]

    # Use product to generate all combinations of these tuples
    combinations = itertools.product(*possibilities)

    # Convert tuples back to lists
    return [list(comb) for comb in combinations]

# Example usage:
print(foo([-4]))        # Output: [[4], [-4]]
print(foo([1, 1]))      # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))     # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))  # Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], ...]
