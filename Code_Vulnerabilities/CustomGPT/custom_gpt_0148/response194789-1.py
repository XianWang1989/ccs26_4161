
import itertools

def foo(lst):
    # Create a list of tuples with positive and negative versions of each number
    possibilities = [(abs(num), -abs(num)) for num in lst]

    # Use itertools.product to generate all combinations
    result = list(itertools.product(*possibilities))

    # Convert tuples to lists
    return [list(item) for item in result]

# Example usage
print(foo([-4]))            # [[4], [-4]]
print(foo([1, 1]))         # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))        # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))     # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]
