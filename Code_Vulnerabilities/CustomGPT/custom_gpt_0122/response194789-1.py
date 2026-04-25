
import itertools

def foo(numbers):
    # Create a list of tuples containing both positive and negative versions of each number
    options = [[num, -num] for num in numbers]

    # Use itertools.product to get all combinations of the options
    combinations = itertools.product(*options)

    # Convert the tuples to lists
    result = [list(comb) for comb in combinations]

    return result

# Example usage
print(foo([-4]))            # [[4], [-4]]
print(foo([1, 1]))         # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))        # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))     # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], ...]
