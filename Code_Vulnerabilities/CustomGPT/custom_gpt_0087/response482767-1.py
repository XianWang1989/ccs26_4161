
from itertools import product

# List of numbers
numbers = [-4, -2, 1, 2, 5, 0]

# Using itertools.product to generate all combinations
result = [t for t in product(numbers, repeat=3) if sum(t) == 0]

print(result)
