
from itertools import product

# List to sample tuples from
numbers = [-4, -2, 1, 2, 5, 0]

# Generating tuples using product and filtering by sum
result = [(i, j, k) for i, j, k in product(numbers, repeat=3) if i + j + k == 0]

print(result)
