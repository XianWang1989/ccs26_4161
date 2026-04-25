
from itertools import product

def foo(lst):
    # Generate all combinations of positive and negative versions of each number
    return [list(comb) for comb in product(*([[abs(x), -abs(x)] for x in lst]))]

# Example usage
print(foo([-4]))            # [[4], [-4]]
print(foo([1, 1]))         # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))        # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))     # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [1, 1, 1]]
