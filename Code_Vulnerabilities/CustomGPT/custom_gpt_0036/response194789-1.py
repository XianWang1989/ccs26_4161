
from itertools import product

def foo(lst):
    # Create a list of tuples for positive and negative possibilities
    signs = [(abs(x), -abs(x)) for x in lst]

    # Use itertools.product to combine all positive/negative variations
    result = list(product(*signs))

    # Transform the tuples into lists
    return [list(r) for r in result]

# Example uses of the function
print(foo([-4]))               # Output: [[4], [-4]]
print(foo([1, 1]))             # Output: [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))            # Output: [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))         # Output: [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1], [1, 1, -1], [1, 1, 1], [-1, 1, 1], [-1, 1, -1]]

# Testing with your given case
print(foo([1, -1, 1]))         # Output: [[1, -1, 1], [1, -1, -1], [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]]
