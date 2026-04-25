
from itertools import product

# Source list
numbers = [-4, -2, 1, 2, 5, 0]

# Using product to generate all combinations of three elements and filtering them
result = [(i, j, k) for i, j, k in product(numbers, repeat=3) if sum((i, j, k)) == 0]

print(result)
