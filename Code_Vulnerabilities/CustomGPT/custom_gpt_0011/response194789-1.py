
from itertools import product

def foo(numbers):
    # Generate all combinations of positive and negative for the input list
    possibilities = list(product(*[ [abs(num), -abs(num)] for num in numbers ]))

    # Convert tuples to lists
    return [list(possibility) for possibility in possibilities]

# Testing the function
print(foo([-4]))            # [[4], [-4]]
print(foo([1, 1]))         # [[1, 1], [1, -1], [-1, 1], [-1, -1]]
print(foo([-1, 3]))        # [[1, 3], [1, -3], [-1, 3], [-1, -3]]
print(foo([1, -1, 1]))     # [[1, -1, 1], [1, -1, -1], [-1, -1, 1], [-1, -1, -1]]
