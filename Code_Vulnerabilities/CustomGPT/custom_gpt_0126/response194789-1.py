
from itertools import product

def foo(lst):
    # Create a list of positive and negative versions of each number
    possibilities = [[abs(num), -abs(num)] for num in lst]

    # Use itertools.product to get the cartesian product of the lists
    result = list(product(*possibilities))

    return result

# Example usage
print(foo([-4]))               # [[4], [-4]]
print(foo([1, 1]))             # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))            # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))         # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]
