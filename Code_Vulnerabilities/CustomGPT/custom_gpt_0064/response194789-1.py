
import itertools

def foo(numbers):
    # Create a list of tuples representing positive and negative versions of the input numbers
    possibilities = [(abs(num), -abs(num)) for num in numbers]

    # Use itertools.product to get all combinations of positive and negative
    combinations = list(itertools.product(*possibilities))

    return [list(comb) for comb in combinations]

# Example usages
print(foo([-4]))          # [[4], [-4]]
print(foo([1, 1]))        # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))       # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))    # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], ...]
