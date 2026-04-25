
from itertools import product

# List of numbers
numbers = [-4, -2, 1, 2, 5, 0]

# Using itertools.product to create tuples and filter by sum
result = [tuple(triplet) for triplet in product(numbers, repeat=3) if sum(triplet) == 0]

# Output result
print(result)
