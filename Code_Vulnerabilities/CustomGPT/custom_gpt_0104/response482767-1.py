
from itertools import product

# Your input list
elements = [-4, -2, 1, 2, 5, 0]

# Generating three-element tuples and filtering those whose sum is 0
result = [(i, j, k) for i, j, k in product(elements, repeat=3) if sum([i, j, k]) == 0]

# Printing the result
print(result)
