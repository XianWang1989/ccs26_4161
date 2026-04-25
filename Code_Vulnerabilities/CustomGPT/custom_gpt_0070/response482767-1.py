
from itertools import product

# List of numbers
numbers = [-4, -2, 1, 2, 5, 0]

# Using itertools.product to create tuples and filter them
result = [(i, j, k) for i, j, k in product(numbers, repeat=3) if sum((i, j, k)) == 0]

# Output the result
print(result)
