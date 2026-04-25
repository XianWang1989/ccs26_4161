
import itertools

def foo(lst):
    # Create a list of tuples representing positive and negative forms
    possibilities = [(abs(num), -abs(num)) for num in lst]

    # Generate all combinations using itertools.product
    all_combinations = list(itertools.product(*possibilities))

    # Convert tuples to lists
    result = [list(combination) for combination in all_combinations]

    return result

# Example usages
print(foo([-4]))         # [[4], [-4]]
print(foo([1, 1]))       # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))      # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))   # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1]]
