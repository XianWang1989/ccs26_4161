
import itertools

def foo(nums):
    # Generate a list of tuples with both positive and negative versions of the numbers
    possibilities = [(abs(num), -abs(num)) for num in nums]

    # Use itertools.product to get all combinations of the possibilities
    combinations = list(itertools.product(*possibilities))

    # Convert tuples to lists
    result = [list(combination) for combination in combinations]

    return result

# Example usage
print(foo([-4]))          # [[4], [-4]]
print(foo([1, 1]))        # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))       # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))    # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]
